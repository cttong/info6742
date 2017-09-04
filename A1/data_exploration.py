# coding: utf-8

get_ipython().system(' cd ../.. && mkdir CMV && cd CMV && curl -# -O https://chenhaot.com/data/cmv/cmv_20161111.jsonlist.gz && gunzip cmv_20161111.jsonlist.gz ')

import glob
import json
import pickle

def has_delta(comment_text):
    if '∆' in comment_text:
        return True
    else:
        return False

if __name__ == '__main__':
    data = glob.glob('../../CMV/*')[0] # Get string for JSON file with data

    f = open(data, 'rb')
    posts_dict = {}
    comments_dict = {}
    for line in f:
        post = json.loads(line.decode('utf-8'))
        post_info = {
                     'title': post['title'],
                     'text': post['selftext'],
                     'author': post['author'],
                     'num_comments': post['num_comments'],
                     'time': post['created'],
                     'url': post['url'],
                     'name': post['name'],
                     'score': post['score']
        }
        comment_list = []
        for c in post['comments']:
            try:
                comment_list.append({
                    'id': c['id'],
                    'author': c['author'],
                    'time': c['created'],
                    'text': c['body'],
                    'parent': c['parent_id'],
                    'score': c['score'],
                    'delta': has_delta(c['body'])

                })
        except: # Skip comments if they do not have these attributes
            pass
        posts_dict[post['id']] = post_info
        comments_dict[post['id']]= comment_list
    f.close()

    # Store new version in pickle
    pickle.dump(posts_dict, open('post_info.p','wb'))
    pickle.dump(comments_dict, open('comment_info.p','wb'))
