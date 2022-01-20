class ISBN:

    def check_ISBN(self, number):
        number_list = list(map(lambda el: int(el) ,list(number.replace("-",""))))
        if len(number_list)==13:
            return (sum(number_list[::2])+sum(list(map(lambda el: el*3 ,number_list[1::2]))))%10==0
        else:
            return False
