/* OffCam — Mock-Daten. Alle Profile sind fiktiv. */

const CREATORS = [
  {
    id: "mia",
    name: "Mia",
    age: 24,
    city: "Berlin",
    km: 4,
    emoji: "🏋️‍♀️",
    ha: 348, hb: 18,
    followers: "128k",
    goal: "collabs",
    goalLabel: "Sucht Collabs",
    tags: ["Fitness", "Lifestyle"],
    bio: "Gym um 6, Content um 9. Suche Leute, die beides ernst nehmen.",
    likesYou: true,
    opener: "Endlich mal ein Match, das nicht nach meinem Rabattcode fragt. 😄",
    replies: [
      "Collab-Idee: Partner-Workout, aber wer zuerst lacht, schneidet das Video. Deal?",
      "Bin gleich im Gym — schreib mir, ich antworte zwischen den Sätzen. 🏋️‍♀️"
    ]
  },
  {
    id: "lena",
    name: "Lena",
    age: 26,
    city: "Hamburg",
    km: 12,
    emoji: "🎭",
    ha: 268, hb: 320,
    followers: "89k",
    goal: "both",
    goalLabel: "Dates & Collabs",
    tags: ["Cosplay", "Craft"],
    bio: "Nähmaschine > Netflix. Con-Season ist Dating-Season.",
    likesYou: true,
    opener: "Sag jetzt bitte nicht, dass du noch nie auf einer Con warst. 🎭",
    replies: [
      "Ich nähe gerade ein Kostüm mit 3.000 Pailletten. Schick Kaffee oder Motivation.",
      "Duo-Cosplay wäre content-technisch übrigens ein Jackpot. Nur so."
    ]
  },
  {
    id: "nova",
    name: "Nova",
    age: 25,
    city: "Köln",
    km: 28,
    emoji: "🖤",
    ha: 285, hb: 250,
    followers: "210k",
    goal: "dates",
    goalLabel: "Sucht Dates",
    tags: ["Alt", "Aesthetic"],
    bio: "Zu viel Eyeliner, zu wenig Zeit. Off cam eigentlich schüchtern.",
    likesYou: false,
    opener: "Hey. Du wirkst weniger anstrengend als mein Feed. Beweis es. 🖤",
    replies: [
      "Ich warne dich: Meine Idee von Romantik ist Friedhofs-Spaziergang plus Espresso.",
      "Schüchtern heißt: Ich schreibe erst witzig, wenn ich dich mag. Das hier zählt schon."
    ]
  },
  {
    id: "emmy",
    name: "Emmy",
    age: 23,
    city: "München",
    km: 7,
    emoji: "🎮",
    ha: 200, hb: 160,
    followers: "45k",
    goal: "both",
    goalLabel: "Dates & Collabs",
    tags: ["Gaming", "Streaming"],
    bio: "Twitch nachts, Backstage tagsüber. Duo-Queue fürs Leben gesucht.",
    likesYou: true,
    opener: "Wichtigste Frage zuerst: Ranked oder Casual — im Leben, mein ich. 🎮",
    replies: [
      "Wenn du bei Mario Kart absichtlich verlierst, merke ich das. Und es zählt als Red Flag.",
      "Stream fängt gleich an. Danach Raid auf deinen Chat? 😌"
    ]
  },
  {
    id: "jules",
    name: "Jules",
    age: 27,
    city: "Leipzig",
    km: 33,
    emoji: "📸",
    ha: 32, hb: 355,
    followers: "33k",
    goal: "collabs",
    goalLabel: "Sucht Collabs",
    tags: ["Boudoir", "Foto"],
    bio: "Ich shoote andere schöner, als sie sich selbst sehen.",
    likesYou: false,
    opener: "Ich hab dein Profil gesehen und direkt drei Shooting-Ideen. Zeit für keine davon. 📸",
    replies: [
      "Golden Hour ist nicht verhandelbar. Alles andere schon.",
      "Portfolio gegen Portfolio — wer zuerst zoomt, verliert."
    ]
  },
  {
    id: "sofia",
    name: "Sofia",
    age: 28,
    city: "Wien",
    km: 51,
    emoji: "✨",
    ha: 315, hb: 35,
    followers: "156k",
    goal: "dates",
    goalLabel: "Sucht Dates",
    tags: ["Fashion", "Spicy"],
    bio: "Wien ist zu klein für anonyme Dates. Deshalb hier.",
    likesYou: true,
    opener: "Du bist also auch hier, weil normale Apps ein Minenfeld sind. Willkommen. ✨",
    replies: [
      "Erstes Date bei mir heißt: Kaffeehaus, zwei Stunden, Handys bleiben in der Tasche.",
      "Ich merke mir alles, was du schreibst. Berufskrankheit. Streng dich an. 😉"
    ]
  },
  {
    id: "kim",
    name: "Kim",
    age: 25,
    city: "Zürich",
    km: 63,
    emoji: "🥗",
    ha: 130, hb: 90,
    followers: "72k",
    goal: "both",
    goalLabel: "Dates & Collabs",
    tags: ["Fitness", "Food"],
    bio: "Meal prep für zwei wäre auch mal schön.",
    likesYou: false,
    opener: "Ehrliche Frage: Kochst du, oder bestellst du nur ästhetisch? 🥗",
    replies: [
      "Sonntag ist Meal-Prep-Tag. Wer hilft, darf probieren. Wer nur zuschaut, wird Content.",
      "Zürich ist teuer, aber mein Kaffee-Spot ist es wert. Irgendwann zeig ich ihn dir."
    ]
  },
  {
    id: "ari",
    name: "Ari",
    age: 24,
    city: "Frankfurt",
    km: 19,
    emoji: "🎙️",
    ha: 220, hb: 280,
    followers: "51k",
    goal: "collabs",
    goalLabel: "Sucht Collabs",
    tags: ["ASMR", "Musik"],
    bio: "Flüstere beruflich. Rede privat sehr gern laut.",
    likesYou: true,
    opener: "Deine Stimme kenn ich noch nicht. Das ist bei mir quasi ein Blind Date. 🎙️",
    replies: [
      "Collab-Pitch: Du redest, ich mache daraus etwas, das 2 Mio. Leuten beim Einschlafen hilft.",
      "Ich nehme gerade auf — flüster mir was, ich antworte in einer Stunde. 🤫"
    ]
  }
];

const TEAM_CHAT = {
  id: "team",
  name: "Team OffCam",
  initial: "O",
  ha: 10, hb: 40,
  verified: true,
  opener: "Willkommen bei OffCam! 🎬 Das hier ist die klickbare Demo: Swipe im Entdecken-Tab, sammle Matches, schreib ihnen. Alles Mock-Daten, nichts verlässt deinen Browser.",
  replies: [
    "Wir lesen alles, versprochen. Aber die spannenderen Chats entstehen im Entdecken-Tab. 😉",
    "Feature-Wünsche? Her damit — die Roadmap für v1 ist noch warm."
  ]
};

const GENERIC_REPLIES = [
  "Haha okay, das merk ich mir. 😄",
  "Bin gerade am Drehen — erzähl weiter, ich lese mit. 🎬",
  "Das klingt verdächtig nach einem Date-Vorschlag. Ich bin nicht abgeneigt.",
  "Du tippst schneller als mein Schnitt rendert. Gefällt mir."
];
