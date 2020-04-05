"""
Proxy design pattern: It allows you to provide the replacement of
an another objects.
The most important part is that here we create an object having original object functionality to provide to the outer
world.
"""


class College:

    def study_in_college(self):
        print("Studying in college")


class CollegeProxy:
    """
    Proxy method
    """
    def __init__(self):
        self.fee_balance = 1000
        self.college = None

    def study_in_college(self):
        """
        proxy in action
        :return:
        """
        if self.fee_balance <=500:
            self.college = College()
            self.college.study_in_college()

        else:
            print("Fee is pending, please pay")


if __name__ == "__main__":
    college_proxy = CollegeProxy()
    college_proxy.study_in_college()
    college_proxy.fee_balance = 100
    college_proxy.study_in_college()
