import pickle
import json

def get_cols():
    with open('skincare_recommendation_model.pkl', 'rb') as f:
        m = pickle.load(f)
    df = m.get('df_clean')
    with open('cols.json', 'w') as f2:
        json.dump({
            "columns": df.columns.tolist(),
            "sample": df.head(1).to_dict('records')
        }, f2, indent=2)

if __name__ == '__main__':
    get_cols()
