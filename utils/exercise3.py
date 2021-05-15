TEXT = (
    'afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithcons'
    'istencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinkn'
    'owinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtoda'
    'yahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocrate'
    'sandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreati'
    'stobemisunderstood'
)


def find_palindromes(t=TEXT):
    palindromes = []
    for i in range(0, len(t)-2):
        for j in range(i+2, len(t)):
            chain = t[i:j]
            if chain == chain[::-1]:
                palindromes.append(chain)
    return palindromes


if __name__ == '__main__':
    print(find_palindromes())
