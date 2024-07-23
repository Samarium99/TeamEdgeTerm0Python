info = {
    "name": "Chrysanthemum",
    "age": 17,
    "hobbies": ["flowering", "stretching to the sun", "eating mosquitos","tanning","practicing carnivorism"],
    "knows_python": True,
    "scores": {
        "carnivorism_and_its_religious_practices": 100,
        "Photosynthesis_101": 30
    }
}
fav_hobby = info['hobbies'][1]
# Use a formatted string to create the output
print(f"Today, I met a plant named {info["name"]}. It was an interesting specimen. Its been living for {info['age']} years (but that will end soon). {info["name"]}'s favorite hobby is {fav_hobby} -- I think it should start a career in yoga. What I find most interesting about {info["name"]} is that IT LIKES {info['hobbies'][2].upper} AND {info['hobbies'][4].upper}, AND IT HAS A  {info['scores']['Photosynthesis_101']} in Photosynthesis 101. A CLASS THAT IT HAS BEEN TAKING FOR {info['age']} YEARS.")