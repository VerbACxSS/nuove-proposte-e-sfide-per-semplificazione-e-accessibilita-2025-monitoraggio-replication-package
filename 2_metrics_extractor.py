import json

import pandas as pd
from tqdm import tqdm

from italian_ats_evaluator import TextAnalyzer, SimplificationAnalyzer
from italian_ats_evaluator.models.TextEvaluation import TextEvaluation
from italian_ats_evaluator.models.SimilarityEvaluation import SimilarityEvaluation
from italian_ats_evaluator.models.DiffEvaluation import DiffEvaluation


def extract_metrics(text: str, result: TextEvaluation, similarity_results: SimilarityEvaluation =None, diff_results: DiffEvaluation = None):
    metrics = {
        'n_tokens': result.basic_evaluation.n_tokens,
        'n_tokens_all': result.basic_evaluation.n_tokens_all,
        'n_chars': result.basic_evaluation.n_chars,
        'n_chars_all': result.basic_evaluation.n_chars_all,
        'n_syllables': result.basic_evaluation.n_syllables,
        'n_words': result.basic_evaluation.n_words,
        'n_unique_lemmas': result.basic_evaluation.n_unique_lemmas,
        'n_sentences': result.basic_evaluation.n_sentences,
        # Pos
        'n_other': result.pos_evaluation.n_other,
        'n_nouns': result.pos_evaluation.n_nouns,
        'n_verbs': result.pos_evaluation.n_verbs,
        'n_number': result.pos_evaluation.n_number,
        'n_symbols': result.pos_evaluation.n_symbols,
        'n_adverbs': result.pos_evaluation.n_adverbs,
        'n_articles': result.pos_evaluation.n_articles,
        'n_pronouns': result.pos_evaluation.n_pronouns,
        'n_particles': result.pos_evaluation.n_particles,
        'n_adjectives': result.pos_evaluation.n_adjectives,
        'n_prepositions': result.pos_evaluation.n_prepositions,
        'n_proper_nouns': result.pos_evaluation.n_proper_nouns,
        'n_punctuations': result.pos_evaluation.n_punctuations,
        'n_interjections': result.pos_evaluation.n_interjections,
        'n_coordinating_conjunctions': result.pos_evaluation.n_coordinating_conjunctions,
        'n_subordinating_conjunctions': result.pos_evaluation.n_subordinating_conjunctions,
        # Verbs
        'n_active_verbs': result.verbs_evaluation.n_active_verbs,
        'n_passive_verbs': result.verbs_evaluation.n_passive_verbs,
        'n_reflective_verbs': result.verbs_evaluation.n_reflective_verbs,
        # Lexicon
        'n_latinisms': result.lexicon_evaluation.n_latinisms,
        'n_difficult_connectives': result.lexicon_evaluation.n_difficult_connectives,
        'n_vdb': result.lexicon_evaluation.n_easy_tokens,
        'n_vdb_fo': result.lexicon_evaluation.n_easy_fo_tokens,
        'n_vdb_au': result.lexicon_evaluation.n_easy_au_tokens,
        'n_vdb_ad': result.lexicon_evaluation.n_easy_ad_tokens,
        # Readability
        'ttr': result.readability_evaluation.ttr,
        'gulpease': result.readability_evaluation.gulpease,
        'flesch_vacca': result.readability_evaluation.flesch_vacca,
        'lexical_density': result.readability_evaluation.lexical_density,
    }
    raw_data = {
        'tokens': result.basic_evaluation.tokens,
        'lemmas': result.basic_evaluation.lemmas,
        'difficult_connectives': [t.text for t in result.lexicon_evaluation.difficult_connectives],
        'latinisms': [t.text for t in result.lexicon_evaluation.latinisms],
    }
    if similarity_results is not None and diff_results is not None:
        metrics.update({
            'semantic_similarity': similarity_results.semantic_similarity,
            'editdistance': diff_results.editdistance,
            'n_added_tokens': diff_results.n_added_tokens,
            'n_deleted_tokens': diff_results.n_deleted_tokens,
            'n_added_vdb_tokens': diff_results.n_added_vdb_tokens,
            'n_deleted_vdb_tokens': diff_results.n_deleted_vdb_tokens,
        })
    return metrics, raw_data


if __name__ == "__main__":
    DATASETS = [
        {
            "name": "text",
            "texts": ['text']
        },
        {
            "name": "comparison",
            "texts": ['text', 'text2']
        },
        {
            "name": "simplification",
            "texts": ['text', 'proofreading', 'lex', 'connectives', 'expressions', 'sentence_splitter', 'nominalizations', 'verbs', 'sentence_reorganizer']
        }
    ]

    for DATASET in DATASETS:
        text_analyzer = TextAnalyzer()
        simplification_analyzer = SimplificationAnalyzer()

        # Load the dataset
        corpus_df = pd.read_excel(f"./filtered/{DATASET['name']}.xlsx")

        # Extract metrics
        for TEXT in DATASET['texts']:
            metrics = []
            raw_data = []
            print(f"Processing {TEXT}...")
            for row in tqdm(corpus_df.to_dict(orient="records")):
                if TEXT == 'text':
                    result = text_analyzer.analyze(row[TEXT])
                    metrics.append(extract_metrics(row[TEXT], result)[0])
                    raw_data.append(extract_metrics(row[TEXT], result)[1])
                else:
                    result = simplification_analyzer.analyze(row[DATASET['texts'][0]], row[TEXT])
                    metrics.append(extract_metrics(row[TEXT], result.simplified_text_evaluation, result.similarity_evaluation, result.diff_evaluation)[0])
                    raw_data.append(extract_metrics(row[TEXT], result.simplified_text_evaluation)[1])

            # Save
            pd.DataFrame(metrics).to_csv(f"./metrics/{DATASET['name']}/{TEXT}_metrics.csv", index=False)
            json.dump(raw_data, open(f"./metrics/{DATASET['name']}/{TEXT}_raw_data.json", "w", encoding="utf-8"), ensure_ascii=False)