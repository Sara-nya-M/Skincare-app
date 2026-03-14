import pickle
import sys

def inspect():
    model_path = 'skincare_recommendation_model.pkl'
    with open('model_info.txt', 'w') as out:
        try:
            with open(model_path, 'rb') as f:
                model = pickle.load(f)
            out.write(f"Model type: {type(model)}\n")
            
            if isinstance(model, dict):
                out.write(f"Keys in dict: {list(model.keys())}\n")
                for k, v in model.items():
                    out.write(f"\n--- Key: {k} ---\n")
                    out.write(f"Type: {type(v)}\n")
                    if hasattr(v, 'feature_names_in_'):
                        out.write(f"Features in: {list(v.feature_names_in_)}\n")
                    if hasattr(v, 'get_feature_names_out'):
                        try:
                            # only first 20 if too long
                            features_out = list(v.get_feature_names_out())
                            out.write(f"Features out (first 50): {features_out[:50]}\n")
                            out.write(f"Total features out: {len(features_out)}\n")
                        except:
                            pass
                    if hasattr(v, 'classes_'):
                        out.write(f"Classes: {v.classes_}\n")
            else:
                out.write("Model is not a dict.\n")
                    
        except Exception as e:
            out.write(f"Error loading model: {e}\n")

if __name__ == '__main__':
    inspect()
