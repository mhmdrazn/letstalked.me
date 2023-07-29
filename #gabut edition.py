#exception pt 2.

name = input('Siapa nama kamu? ')
print(f'Hai {name}! Selamat datang! Selamat berbelanja!.')

answer = ' '
answer = input('apakah anda ingin melanjutkan hidup khayalan ini? (iya/tidak) ').lower()

while answer == 'iya' and 'tidak':
    if answer == 'iya':
        print('selamat menjelajahi dunia fantasy ini!')
        break
    elif answer == 'tidak':
        print('jika tidak wah kamu telalu lelah yah sepertinya untuk berkhayal 😔')
    else:
        print('aku gak paham')

if answer == 'iya':
    print('apa yang membuat anda tertarik untuk mengikuti kegiatan membosankan ini?')
    input('> ')
    print('terimakasih loh ya 🤪🤗🤗')
    input('')
    age = input("oiya nih bro, umur lu berapa? ")
    if age > '25':
        print('wah, tua bgt ya lu wkwk')
    elif age < '25':
        print('azik, muda mudi nih bozz')
    input('')
    input('masukin tgl lahir lu brodi, tenang gk bakal dijual kok, mau ak itungin udah berapa hari lu idup di dunia yg kejam ini, sokin: ')
