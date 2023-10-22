from translate import Translator

def get_income(translator):
    monthly_income = float(input(translator.translate("What is your monthly income?: ")))
    return monthly_income

def get_savings_percentage(monthly_income):
    savings_percentage = 30
    savings = (savings_percentage / 100) * monthly_income
    return savings

def get_housing_percentage(monthly_income):
    housing_percentage = 25
    housing = (housing_percentage / 100) * monthly_income
    return housing

def get_personal_expenses(monthly_income):
    personal_percentage = 20
    personal = (personal_percentage / 100) * monthly_income
    return personal

def get_miscellaneous_expenses(monthly_income):
    miscellaneous_percentage = 25
    miscellaneous_bill = (miscellaneous_percentage / 100) * monthly_income
    return miscellaneous_bill

def main():
    Language_question = input("Language/idioma/语言?: ")

    if Language_question == "Spanish":
        translator = Translator(to_lang='es')
    elif Language_question == "English":
        translator = Translator(to_lang='en')
    elif Language_question == "Chinese":
        translator = Translator(to_lang='zh')
    else:
        print("This language is not available currently")
        return

    monthly_income = get_income(translator)
    housing_savings = get_housing_percentage(monthly_income)
    personal_savings = get_personal_expenses(monthly_income)
    savings = get_savings_percentage(monthly_income)
    misc_bills = get_miscellaneous_expenses(monthly_income)

    print(translator.translate(f"Based on your monthly income of {monthly_income:.2f} dollars"))
    print(translator.translate(f"You should use {housing_savings:.2f} dollars for housing"))
    print(translator.translate(f"You should use {personal_savings:.2f} dollars for personal expenses"))
    print(translator.translate(f"You should use {misc_bills:.2f} dollars for miscellaneous expenses"))
    print(translator.translate(f"You should save {savings:.2f} dollars"))
    
if __name__ == "__main__":
    main()




            
            


        