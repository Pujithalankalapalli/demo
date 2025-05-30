from abc import ABC, abstractmethod
class My(ABC):
    @abstractmethod
    def post(self):
        pass
def vote():
    age = int(input("Enter Age for vote: "))
    if age >= 18:
        print("You are eligible")
    else:
        print("You are not eligible")
vote()