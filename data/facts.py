from random import choice

facts = [
    ' Axe, Disruptor, Warlock и Lifestealer принадлежат к одной расе – Oglodi.',
    'Beastmaster и Lycan росли в одном королевстве.',
    'Axe стал генералом, обезглавливая своих военачальников. Когда он достиг вершины, обезглавливать стало некого. Axe остался один в своей армии.',
    ' Pudge поручили расчленять трупы, чтобы очистить поле боя. В итоге он стал каннибалом-психопатом.',
    ' Неясно, жив Kunnka или нет.'
    'Omniknight является верным членом церкви Омнистологии.',
    ' Doompng – дикие существа, сбежавшие из глубин ада. Многие из этих созданий были приручены в качестве курьеров. Возможно, что бы посмеяться над DOOM.',
    'Отец Brewmaster является небожителем.',
    'Любимый скакун Chaos Knight – Армаггедон.',
    ' Бог Undying, Бог Мертвых, разрушил монастырь Anti-Mage. Несмотря на это, Anti-Mage все равно настаивает на убийстве INT-героев, а не STR-героев.',
    'Многие охотились за бесценными рогами Magnus. Он пронзил и растоптал бесчисленное количество таких охотников.',
    ' Город Timbersaw был уничтожен живыми деревьями по неизвестной причине. Теперь Timbersaw ненавидит деревья.',
    'Tusk поручили миссию – найти самую эпичную битву. Именно поэтому он отправился на войну Древних. Награда? Конечно, бесплатная выпивка!',
    'Earth Spirit – это дух, которому стало скучно, и он вселился в статую генерала армии.',
    ' Anti-Mage ненавидит магию.',
    'Bloodseeker обожает казни и виселицы.',
    'Любимого зверя Mirana зовут Sagan.',
    ' Morphpng теряет память после каждой смены формы.',
    'Жрецы Clasz должны были удалить свои глаза. К счастью, Faceless Void нечего было удалять.',
    'Phantom Lancer был рыбаком, пока война не пришла в его деревню и ему не пришлось убить злого волшебника.\n С последним вздохом мага Phantom Lancer получил свои невероятные силы.',
    'Нет причин и обьяснений, почему и кого убивает Phantom Assassin. Они просто считают обычным делом время от времени убивать простых людей.',
    'Riki - член клуба «Мы убиваем лишь тех, кто заслуживает смерти».',
    ' Clinkz и Shadow Shaman родом из одного региона.',
    'Бабушка Sniper – Gramma Sharpie. А его дед – Brag ‘Whistlecheeks’ Sharpeye.',
    'Один из зверей Luna – Avon – был воспитан ее основным питомцем Nova.',
    'Ursa владеет двумя Bpnk Dagger, но использует их как подтяжки.',
    'У Lone Druid есть ребенок (возможная отсылка к Invoker).'

]


def generate_facts():
    return choice(facts)