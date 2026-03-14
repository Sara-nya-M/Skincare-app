import pickle

def test_inference():
    with open('skincare_recommendation_model.pkl', 'rb') as f:
        m = pickle.load(f)
    
    skin_type_dict = m.get('skin_type_ingredients', {})
    skin_concern_dict = m.get('skin_concern_ingredients', {})
    
    print("Skin type first item:")
    first_type = list(skin_type_dict.keys())[0] if skin_type_dict else None
    print(f"- Key: {first_type}")
    print(f"- Value: {skin_type_dict.get(first_type)}")
    print(f"- Value Type: {type(skin_type_dict.get(first_type))}")
    
    print("Skin concern first item:")
    first_concern = list(skin_concern_dict.keys())[0] if skin_concern_dict else None
    print(f"- Key: {first_concern}")
    print(f"- Value: {skin_concern_dict.get(first_concern)}")
    print(f"- Value Type: {type(skin_concern_dict.get(first_concern))}")
    
if __name__ == '__main__':
    test_inference()
