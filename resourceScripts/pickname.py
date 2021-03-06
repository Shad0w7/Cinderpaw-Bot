# pickname.py
import random

prefixList = [
'Acorn',
'Adder',
'Amber',
'Ant',
'Apple',
'Arch',
'Ash',
'Aspen',
'Badger',
'Bark',
'Beech',
'Beetle',
'Berry',
'Birch',
'Bird',
'Black',
'Blizzard',
'Blossom',
'Blue',
'Boulder',
'Bounce',
'Bracken',
'Branch',
'Bramble',
'Brave',
'Breeze',
'Briar',
'Bright',
'Brindle',
'Broken',
'Brown',
'Brush',
'Bumble',
'Buzzard',
'Cedar',
'Cherry',
'Cinder',
'Claw',
'Cloud',
'Cloudy',
'Clover',
'Coal',
'Cold',
'Copper',
'Creek',
'Cricket',
'Crooked',
'Crow',
'Daisy',
'Dapple',
'Dappled',
'Dark',
'Dawn',
'Dead',
'Deer',
'Dew',
'Dewy',
'Dove',
'Drift',
'Duck',
'Dusk',
'Dust',
'Dusty',
'Eagle',
'Ebony',
'Echo',
'Eel',
'Egg',
'Fading',
'Falcon',
'Fallen',
'Fallow',
'Fawn',
'Feather',
'Fennel',
'Fern',
'Ferret',
'Finch',
'Fire',
'Fish',
'Flame',
'Fleet',
'Flint',
'Flower',
'Fox',
'Frog',
'Frost',
'Furze',
'Fuzzy',
'Gold',
'Golden',
'Goose',
'Gorse',
'Gray',
'Grass',
'Green',
'Hail',
'Half',
'Hare',
'Hawk',
'Hay',
'Hazel',
'Heather',
'Heavy',
'Heron',
'Hollow',
'Holly',
'Honey',
'Horse',
'Ice',
'Ivy',
'Jagged',
'Jay',
'Jump',
'Juniper',
'Kestrel',
'Kink',
'Lake',
'Larch',
'Lark',
'Leaf',
'Leopard',
'Lichen',
'Light',
'Lightning',
'Lily',
'Lion',
'Little',
'Lizard',
'Long',
'Lost',
'Loud',
'Lynx',
'Maggot',
'Mallow',
'Marsh',
'Maple',
'Meadow',
'Milk',
'Minnow',
'Mint',
'Mink',
'Misty',
'Mole',
'Moon',
'Morning',
'Moss',
'Mossy',
'Moth',
'Mouse',
'Mud',
'Muddy',
'Mumble',
'Nettle',
'Newt',
'Night',
'Nut',
'Oak',
'Oat',
'Odd',
'Olive',
'One',
'Otter',
'Owl',
'Pale',
'Patch',
'Pear',
'Perch',
'Petal',
'Pigeon',
'Pike',
'Pine',
'Plum',
'Pool',
'Poppy',
'Pounce',
'Prickle',
'Puddle',
'Quail',
'Quick',
'Quiet',
'Rabbit',
'Raccoon',
'Ragged',
'Rain',
'Rapid',
'Rat',
'Raven',
'Red',
'Reed',
'Ripple',
'River',
'Robin',
'Rock',
'Rocky',
'Rose',
'Rowan',
'Rubble',
'Running',
'Rush',
'Russet',
'Rust',
'Rusty',
'Rye',
'Sage',
'Scorch',
'Sedge',
'Seed',
'Shade',
'Shadow',
'Sharp',
'Sheep',
'Shell',
'Shining',
'Short',
'Shrew',
'Shred',
'Silent',
'Silver',
'Sky',
'Slate',
'Slow',
'Small',
'Smoke',
'Snail',
'Snake',
'Sneeze',
'Snow',
'Soft',
'Soot',
'Sorrel',
'Spark',
'Sparrow',
'Speckle',
'Spider',
'Splash',
'Spot',
'Spotted',
'Spruce',
'Squirrel',
'Starling',
'Stone',
'Storm',
'Stumpy',
'Sun',
'Sunny',
'Swallow',
'Sweet',
'Swift',
'Tall',
'Talon',
'Tangle',
'Tansy',
'Tawny',
'Thistle',
'Thorn',
'Thrush',
'Thunder',
'Tiger',
'Timber',
'Tiny',
'Toad',
'Torn',
'Trout',
'Tumble',
'Twig',
'Twilight',
'Vine',
'Vole',
'Wasp',
'Weasel',
'Web',
'Weed',
'Wet',
'Whisker',
'White',
'Wild',
'Willow',
'Wind',
'Wolf',
'Yellow',
'Yarrow',]


suffixes = [
'acorn',
'bee',
'belly',
'berry',
'bird',
'blaze',
'branch',
'breeze',
'briar',
'bright',
'brook',
'call',
'claw',
'cloud',
'creek',
'cry',
'dapple',
'dawn',
'dust',
'ear',
'eye',
'eyes',
'face',
'fall',
'fang',
'feather',
'fern',
'fin',
'fire',
'fish',
'flame',
'flight',
'flower',
'foot',
'frost',
'fur',
'gaze',
'goose',
'grass',
'hare',
'hawk',
'heart',
'heather',
'hollow',
'ice',
'ivy',
'jaw',
'jay',
'leaf',
'leap',
'leg',
'light',
'mask',
'mist',
'moon',
'nettle',
'nose',
'nut',
'pad',
'path',
'pelt',
'petal',
'pool',
'poppy',
'puddle',
'rapid',
'run',
'scar',
'shade',
'shine',
'sky',
'snow',
'song',
'spark',
'speck',
'spirit',
'splash',
'spots',
'spring',
'stem',
'step',
'storm',
'streak',
'stream',
'strike',
'stripe',
'sun',
'swipe',
'tail',
'talon',
'thicket',
'thorn',
'throat',
'tooth',
'tree',
'tuft',
'water',
'watcher',
'whisker',
'willow',
'wind',
'wing',
'wish',
'whisper ',]

def warriorName():
    prefixNum = random.randint(0, len(prefixList))
    suffixNum = random.randint(0, len(suffixes))
    return 'Your Randomly Generated Name is: {0}{1}!'.format(prefixList[prefixNum], suffixes[suffixNum])

kittyNames =['Oscar',
'Max',
'Tiger',
'Sam',
'Misty',
'Simba',
'Coco',
'Chloe',
'Lucy',
'Missy',
'Molly',
'Tigger',
'Smokey',
'Milo',
'Cleo',
'Sooty',
'Monty',
'Puss',
'Kitty',
'Felix',
'Bella',
'Jack',
'Lucky',
'Casper',
'Charlie',
'Thomas',
'Toby',
'Ginger',
'Oliver',
'Daisy',
'Gizmo',
'Muffin',
'Jessie',
'Sophie',
'Fluffy',
'Sebastian',
'Billy',
'Jasper',
'Jasmine',
'Sasha',
'Zoe',
'Phoebe',
'Tom',
'Lilly',
'Sylvester',
'George',
'Kimba',
'Harry',
'Holly',
'Minnie',]

def kittypetName():
    number = random.randint(0, len(kittyNames))
    return "Your Kittypet Name is: {}!".format(kittyNames[number])


clans = ['AuroraClan',
'BeamClan',
'BlandClan',
'BlazeClan',
'BlitheClan',
'BlondClan',
'BreezeClan',
'BrightClan',
'ClearClan',
'DawnClan',
'DownyClan',
'DrizzleClan',
'EmberClan',
'ElderClan',
'FadeClan',
'FaintClan',
'FickleClan',
'GladeClan',
'GlareClan',
'GlimmerClan',
'GlossyClan',
'GoldenClan',
'GraceClan',
'IluminateClan',
'LightClan',
'LucentClan',
'LuminousClan',
'LusterClan',
'LustrousClan',
'MerryClan',
'MorningClan',
'MountainClan',
'PaleClan',
'PorousClan',
'PureClan',
'RadiantClan',
'RayClan',
'RiseClan',
'ShineClan',
'ShiningClan',
'SolarClan',
'SparkClan',
'SparkleClan',
'SunlitClan',
'SunnyClan',
'SunriseClan',
'SunsetClan',
'StrikeClan',
'TideClan',
'TorrentClan',
'WaveClan',
'WispClan',
'PhosphorClan ',
'AshClan',
'BaneClan',
'BleakClan',
'BoneClan',
'BurnClan',
'ClawClan',
'CryptClan',
'DarkClan',
'DenseClan',
'DimClan',
'DireClan',
'DismalClan',
'DourClan',
'DuskClan',
'EbonyClan',
'EclipseClan',
'FallenClan',
'GloomClan',
'GlumClan',
'GrimClan',
'HateClan',
'Harshclan',
'Marrowclan',
'MoonlightClan',
'MurkyClan',
'MysticalClan',
'NightClan',
'ParadoxClan',
'PhantomClan',
'ShadeClan',
'ShadowClan',
'SharpClan',
'SilentClan',
'SkullClan',
'SlashClan',
'SmokeClan',
'SootClan',
'SoulClan',
'SpiritClan',
'SullenClan',
'TwilightClan',
'TwistedClan',
'VileClan ',
'AirClan',
'AlgidClan',
'AlgorClan',
'BitterClan',
'BlizzardClan',
'BogClan',
'BoulderClan',
'BreezeClan',
'BriskClan',
'BrookClan',
'CinderClan',
'CloudyClan',
'ColdClan',
'CragClan',
'CreekClan',
'CryoClan',
'DaftClan',
'DewClan',
'DipClan',
'DripClan',
'DrizzleClan',
'EarthClan',
'FireClan',
'FlurryClan',
'FogClan',
'FreezeClan',
'FrigidClan',
'FrostClan',
'FrozenClan',
'GlacialClan',
'GlacierClan',
'GorgeClan',
'HailClan',
'HeatClan',
'IceClan',
'IcyClan',
'LakeClan',
'LightningClan',
'LogClan',
'MarshClan',
'MistClan',
'MossClan',
'MudClan',
'OceanClan',
'PuddleClan',
'RainClan',
'ReedClan',
'RippleClan',
'RiverClan',
'RockClan',
'RumbleClan',
'SandClan',
'SeaClan',
'ShiverClan',
'ShellClan',
'ShoreClan',
'SleetClan',
'SlushClan',
'SnowClan',
'SnowfallClan',
'SnowyClan',
'SplashClan',
'StormClan',
'StreamClan',
'ThunderClan',
'TornadoClan',
'TsunamiClan',
'WaterClan',
'WaveClan',
'WetClan',
'WhirlwindClan',
'WindClan ',
'AcornClan',
'AppleClan',
'AutumnClan',
'BambooClan',
'BeechClan',
'BerryClan',
'BirchClan',
'BrackenClan',
'BrambleClan',
'BreezeClan',
'BriarClan',
'BushClan',
'CaveClan',
'CedarClan',
'ChestnutClan',
'CoalClan',
'CypressClan',
'DappleClan',
'DirtClan',
'EarthClan',
'EastClan',
'FallClan',
'FernClan',
'FirClan',
'FireClan',
'ForestClan',
'GladeClan',
'GrassClan',
'HawthornClan',
'HollowClan',
'HollyClan',
'IvyClan',
'JuniperClan',
'LavaClan',
'MadderClan',
'MapleClan',
'MeadowClan',
'MoonClan',
'MushroomClan',
'NorthClan',
'OakClan',
'OrchardClan',
'PineClan',
'PrimroseClan',
'RootClan',
'RueClan',
'SageClan',
'SandClan',
'SouthClan',
'SpringClan',
'SummerClan',
'SunClan',
'StarClan',
'SycamoreClan',
'TangleClan',
'TiagaClan',
'TimberClan',
'TreeClan',
'TwigClan',
'VineClan',
'WestClan',
'WillowClan',
'WinterClan ',
'BlossomClan',
'BudClan',
'CarnationClan',
'CatmintClan',
'ChiveClan',
'CloverClan',
'DaisyClan',
'FlowerClan',
'HerbClan',
'IrisClan',
'LavenderClan',
'LeafClan',
'LilyClan',
'MintClan',
'OrchidClan',
'PeonyClan',
'PetalClan',
'PoppyClan',
'SageClan',
'StemClan',
'ThornClan',
'TulipClan',
'VioletClan',
'WheatClan',
'YarrowClan ',
'AdderClan',
'BadgerClan',
'BatClan',
'BearClan',
'BeastClan',
'BirdClan',
'CatClan',
'CoyoteClan',
'CritterClan',
'CrowClan',
'DeerClan',
'DogClan',
'DoveClan',
'EagleClan',
'ElkClan',
'FinchClan',
'FishClan',
'FoxClan',
'FrogClan',
'HawkClan',
'HogClan',
'HoundClan',
'JayClan',
'KangarooClan',
'KestrelClan',
'KiteClan',
'LizardClan',
'MiceClan',
'MooseClan',
'MouseClan',
'PantherClan',
'PigClan',
'RavenClan',
'RobinClan',
'RoosterClan',
'SnakeClan',
'SparrowClan',
'ThrushClan',
'TigerClan',
'ViperClan',
'WildClan',
'WrenClan ',
'AmethystClan',
'BlackClan',
'BlueClan',
'BronzeClan',
'CopperClan',
'EmeraldClan',
'GoldClan',
'GrayClan',
'GreenClan',
'GreyClan',
'IndigoClan',
'JadeClan',
'OrangeClan',
'OpalClan',
'PearlClan',
'PinkClan',
'RainbowClan',
'RedClan',
'RubyClan',
'RobinClan',
'SapphireClan',
'SilverClan',
'WhiteClan',
'YellowClan',
'AlphaClan',
'AprilClan',
'AugustClan',
'BravoClan',
'CharlieClan',
'DecemberClan',
'DeltaClan',
'EchoClan',
'FebruaryClan',
'FlightClan',
'FoxtrotClan',
'GolfClan',
'HiddenClan',
'HotelClan',
'IndiaClan',
'JanuaryClan',
'JulietClan',
'JulyClan',
'JuneClan',
'KiloClan',
'LimaClan',
'MarchClan',
'MayClan',
'MikeClan',
'NovemberClan',
'OctoberClan',
'OscarClan',
'PapaClan',
'QuebecClan',
'QuickClan',
'RomeoClan',
'SeptemberClan',
'SierraClan',
'StrayClan',
'TangoClan',
'UniformClan',
'VictorClan',
'WarriorClan',
'WhiskeyClan',
'XrayClan',
'YankeeClan',
'ZuluClan ',]

def clanName():
    xz = random.randint(0, len(clans))
    return "Your Genearated Clan Name is: {}! May it rule across the Forests, Mountains, and Oceans!".format(clans[xz])

