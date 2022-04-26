import os


topic_names = []

###    ------ CREATING THE TOPIC LIST FROM BEGINNING
for subdir, dirs, files in os.walk(
    "/Users/tancetiner/Documents/GitHub/PURE_NLP_2022/files/for_cem/bio_texts"
):
    for file in files:

        filepath = subdir + os.sep + file
        topic_names.append(filepath[filepath.rfind("/") + 1 : filepath.rfind(".")])

###   ------ CREATING THE PREQ TXT FILES
for topic in topic_names:
    with open(
        "/Users/tancetiner/Documents/GitHub/PURE_NLP_2022/files/for_cem/bio_prereqs/{}.txt".format(
            topic
        ),
        "w",
        encoding="utf-8",
    ) as f:
        for topic2 in topic_names:
            if topic != topic2:
                f.write("{};{}\n".format(topic, topic2))
