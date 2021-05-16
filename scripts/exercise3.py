TEXT = (
    'afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithcons'
    'istencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinkn'
    'owinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtoda'
    'yahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocrate'
    'sandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreati'
    'stobemisunderstood'
)


def find_palindromes(text=TEXT):
    """Find palindrome sequences in the given text."""
    palindromes = []
    for i in range(0, len(text)-1):
        for j in range(i+2, len(text)+1):
            chain = text[i:j]
            if chain == chain[::-1]:
                palindromes.append(chain)
    return palindromes


if __name__ == '__main__':
    print(find_palindromes())
