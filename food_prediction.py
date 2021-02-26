from imageai.Prediction import ImagePrediction
import os
import time

#predict_image = "C:/FYDP/image.jpg"
#model_position = "C:/FYDP/resnet50_prediction.h5"
#把模型的地址和要识别图片的地址递给food_dect, return一个list包含识别出的可能的食物
def food_dect(predict_image, model_position):
    list_predict_results= []
    prediction = ImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath(model_position)
    prediction.loadModel()
    predictions, probabilities = prediction.predictImage(predict_image, result_count=5)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        #print(eachPrediction," : ", eachProbability)
        if eachProbability > 3:
            if_fod, name_fod = name_rectify(eachPrediction)
            if if_fod == True:
                list_predict_results = list_predict_results + name_fod
    
    if not list_predict_results:
        list_predict_results.append("can not recognize item")
    list_predict_results = list(dict.fromkeys(list_predict_results))
    return list_predict_results

    

def name_rectify(d_result):
    if_food = False
    r_name = d_result
    l_r_name = []
    list_all_possible_result = [
    "Granny_Smith", "strawberry", "orange", "head_cabbage","lemon","ice_cream", "guacamole",
    "artichoke", "banana", "zucchini", "hip", "pomegranate", "strainer", "cucumber", "meat_loaf",
    "balloon", "jackfruit", "acorn", "pineapple", "custard_apple", "tennis_ball","spaghetti_squash",
    "bell_pepper", "butternut_squash", "broccoli", "cauliflower","corn", "fig", "tomato","blueberry",
    "cherry", "acorn_squash","pumpkin","butternut_squash", "jack-o'-lantern","potato", "bell_pepper",
    "wig","onion","buckeye", "mushroom", "hotdog","carrot"
    ]
    if r_name in list_all_possible_result:
        if_food = True
        if r_name == "Granny_Smith":
            l_r_name.append("apple")
        elif r_name == "strainer":
            l_r_name.append("blackbarry")
        elif r_name == "hip":
            l_r_name.append("cherry")
            l_r_name.append("blueberry")
            l_r_name.append("tomato")
        elif r_name == "balloon":
            l_r_name.append("grapes")
        elif r_name == "acorn":
            l_r_name.append("longan")
        elif r_name == "jackfruit":
            l_r_name.append("jackfruit")
            l_r_name.append("pear")
        elif r_name == "pomegranate":
            l_r_name.append("pomegranate")
            l_r_name.append("peach")
        elif r_name == "tennis_ball":
            l_r_name.append("watermelon")
        elif r_name == "head_cabbage":
            l_r_name.append("cabbage")
        elif r_name == "fig":
            l_r_name.append("fig")
            l_r_name.append("eggplant")
        elif r_name == "spaghetti_squash":
            l_r_name.append("spaghetti_squash")
            l_r_name.append("potato")
        elif r_name == "jack-o'-lantern":
            l_r_name.append("pumpkin")
        elif r_name == "bell_pepper":
            l_r_name.append("pepper")
        elif r_name == "wig":
            l_r_name.append("onion")
        elif r_name == "hotdog":
            l_r_name.append("hotdog")
            l_r_name.append("carrot")
        else:
            l_r_name.append(r_name)

    return if_food, l_r_name


if __name__ == "__main__":
    food_dect("/home/ubuntu/SmartPantryServer/apple.jpg","./resnet50_weights_tf_dim_ordering_tf_kernels.h5")
