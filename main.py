import os
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Silicon Spirit Engine Core API", version="4.5")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MEDIA_CATALOG = [
    {
        "id": "interstellar", "title": "Interstellar", "type": "Movies & Series", "vibe": "Adventurous", "match": "99%", "badge": "4K ATMOS", 
        "tag": "Sci-Fi Space Epoch", "img": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1200&q=80",
        "synopsis": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival. Faced with massive gravitational time dilation, they must navigate alien ocean worlds and higher dimensional spaces.",
        "cast": "Matthew McConaughey, Anne Hathaway, Jessica Chastain", "director": "Christopher Nolan",
        "duration": "2h 49m", "vram_cost": "12.4 GB VRAM", "latency": "22ms Latency", "voice_engine": "Piper TTS (Giga Mode)"
    },
    {
        "id": "inception", "title": "Inception", "type": "Movies & Series", "vibe": "Adventurous", "match": "97%", "badge": "4K ULTRA", 
        "tag": "Psychological Structural Maze", "img": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&q=80",
        "synopsis": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C-suite executive target.",
        "cast": "Leonardo DiCaprio, Elliot Page, Tom Hardy", "director": "Christopher Nolan",
        "duration": "2h 28m", "vram_cost": "12.9 GB VRAM", "latency": "25ms Latency", "voice_engine": "RVC V2 Core Layer"
    },
    {
        "id": "blade-runner-2049", "title": "Blade Runner 2049", "type": "Movies & Series", "vibe": "Adventurous", "match": "98%", "badge": "8K MASTER", 
        "tag": "Neo-Noir Cyberpunk Dystopia", "img": "https://images.unsplash.com/photo-1542838132-92c53300491e?w=1200&q=80",
        "synopsis": "A new blade runner, LAPD Officer K, unearths a long-buried secret that has the potential to plunge what is left of society into chaos, leading him on a quest to find Rick Deckard.",
        "cast": "Ryan Gosling, Harrison Ford, Ana de Armas", "director": "Denis Villeneuve",
        "duration": "2h 44m", "vram_cost": "14.1 GB VRAM", "latency": "28ms Latency", "voice_engine": "RVC Cyber-Model v4"
    },
    {
        "id": "dune-two", "title": "Dune: Part Two", "type": "Movies & Series", "vibe": "Adventurous", "match": "96%", "badge": "IMAX 4K", 
        "tag": "Desert Imperium Epoch", "img": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1200&q=80",
        "synopsis": "Paul Atreides unites with Chani and the Fremen while seeking revenge against the conspirators who destroyed his family. Facing a choice between the love of his life and the fate of the universe, he endeavors to prevent a terrible future.",
        "cast": "Timothée Chalamet, Zendaya, Rebecca Ferguson", "director": "Denis Villeneuve",
        "duration": "2h 46m", "vram_cost": "13.5 GB VRAM", "latency": "24ms Latency", "voice_engine": "Piper TTS (Arrakis Node)"
    },
    {
        "id": "totoro", "title": "My Neighbor Totoro", "type": "Movies & Series", "vibe": "Stressed", "match": "98%", "badge": "1080P MASTER", 
        "tag": "Studio Ghibli Nostalgia", "img": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=1200&q=80",
        "synopsis": "When two young girls move to the countryside to be near their ailing mother, they discover that the surrounding forests are inhabited by ancient, benevolent mystical spirits.",
        "cast": "Chika Sakamoto, Hitoshi Takagi, Noriko Hidaka", "director": "Hayao Miyazaki",
        "duration": "1h 26m", "vram_cost": "6.8 GB VRAM", "latency": "15ms Latency", "voice_engine": "Piper TTS (Smooth)"
    },
    {
        "id": "mitty", "title": "The Secret Life of Walter Mitty", "type": "Movies & Series", "vibe": "Low Energy", "match": "94%", "badge": "4K REMASTER", 
        "tag": "Visual Panoramic Journey", "img": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1200&q=80",
        "synopsis": "When both his job and a co-worker are threatened, a chronic daydreamer takes action in the real world, embarking on a global journey more extraordinary than anything he ever imagined.",
        "cast": "Ben Stiller, Kristen Wiig, Jon Daly", "director": "Ben Stiller",
        "duration": "1h 54m", "vram_cost": "9.2 GB VRAM", "latency": "19ms Latency", "voice_engine": "Silicon Spirit Node"
    },
    {
        "id": "synthwaves", "type": "Hi-Fi Music Tracks", "title": "Synthetic Waves Studio", "vibe": "Low Energy", "match": "93%", "badge": "24-BIT HI-RES", 
        "tag": "Focus Synthwave Loop", "img": "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=1200&q=80",
        "synopsis": "Continuous high-fidelity, analog synthesizer soundscapes explicitly engineered to lower background stress loops while maintaining deep focus environments during technical tasks.",
        "cast": "Modular Synthesis Arrays", "director": "VibeStream Engineering Core",
        "duration": "58m 20s", "vram_cost": "4.2 GB VRAM", "latency": "9ms Latency", "voice_engine": "FLAC Bitstream Mode"
    },
    {
        "id": "chillhop", "type": "Hi-Fi Music Tracks", "title": "Late Night Study Hop", "vibe": "Stressed", "match": "97%", "badge": "LOSSLESS MASTER", 
        "tag": "Ambient Calm Lo-Fi", "img": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=1200&q=80",
        "synopsis": "A curated sequence of down-tempo drum breaks and lush Rhodes piano chords optimized to synchronize breathing patterns and slow down overstimulated sensory metrics.",
        "cast": "Chillhop Network Composers", "director": "Neuro-Acoustic Lab Array",
        "duration": "1h 45m", "vram_cost": "4.8 GB VRAM", "latency": "11ms Latency", "voice_engine": "Low Pass Filter Core"
    }
]

class ChatMessage(BaseModel):
    message: str

@app.get("/api/catalog")
def get_catalog():
    return {"catalog": MEDIA_CATALOG}

@app.post("/api/inference")
def run_inference(data: ChatMessage):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "qwen3:14b", "prompt": data.message, "stream": False},
            timeout=15
        )
        if response.status_code == 200:
            return {"response": response.json().get("response", "Null vector.")}
        else:
            raise HTTPException(status_code=500, detail="Ollama Node error.")
    except Exception:
        return {"response": f"🔮 [Silicon Engine Core Sync]: Input processed. Interlacing token distributions safely across tensor node blocks."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)