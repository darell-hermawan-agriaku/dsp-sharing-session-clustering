from typing import Union

def check_answer_1(
    answer: int
) -> None:
    question = "From the figure above, do you have any guess how many clusters it should be?"
    try:
        assert answer in (4, 5)

    except Exception:
        if answer in (0, 1, 2, 3):
            print("Wrong answer: Less than it should be")
        elif type(answer) == int:
            print("Wrong answer: More than it should be")
        else:
            print("Wrong answer: Bong cap lay, konyo mama koslay !!")
                            
    else:
        print("Good job!")

def check_answer_2(
    answer: int
) -> None:
    question = "Based on the scatter plot above, what is optimal number of clusters should we choose?"
    try:
        assert answer in (4, 5)

    except Exception:
        if answer in (0, 1, 2, 3):
            print("Wrong answer: Less than it should be")
        elif type(answer) == int:
            print("Wrong answer: More than it should be")
        else:
            print("Wrong answer: Please input an integer")
                            
    else:
        print("Good job!")

def check_answer_3(
    answer: Union[bool, str]
) -> None:
    question = "Is there any way to know what is the optimal and absolute number of clusters, such as advanced elbow-method?"
    try:
        assert bool(answer) == True

    except Exception:
       print("Wrong answer:\n\nBecause clustering is unsupervised learning, we always don't know the right answer for this.\nHuman intervention is always the best solution.")
                            
    else:
        print("Right answer")

