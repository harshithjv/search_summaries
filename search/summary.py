"""
summary.py
"""

import json
import re


def get_summaries():
    """
    TODO: Function description
    """
    summaries = None
    with open('data.json') as data:
        data = json.load(data)
        summaries = data['summaries']
    return summaries


def search_summaries(search_string, k=5):
    """
    TODO: Function description
    """
    summaries = get_summaries()
    search_splits = search_string.split()
    search_splits_len = len(search_splits)

    full_matches = []
    split_matches = []
    partial_matches = []
    result_counts = 0
    for summary in summaries:
        regex = re.compile(r"\s"+search_string+r"[\s\.]", re.I)
        summary_text = summary["summary"]
        found_items = regex.findall(summary_text)
        if found_items:
            full_matches.append(summary)
            result_counts += 1
        else:
            match_times = 0
            atleast_once = False
            for split_string in search_splits:
                regex2 = re.compile(r"\s"+split_string+r"[\s\.]", re.I)
                found = regex2.findall(summary_text)
                if found:
                    match_times += 1
                    atleast_once = True
                result_counts += 1
            if match_times == search_splits_len:
                split_matches.append(summary)
            elif atleast_once:
                partial_matches.append(summary)
        if result_counts == k:
            break

    all_searches = full_matches
    all_searches.extend(partial_matches)
    all_searches.extend(split_matches)

    return (all_searches, result_counts)
