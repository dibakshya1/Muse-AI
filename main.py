import argparse
import sys
from muse.core.composer import NeuralComposer
from muse.analysis.critic import AestheticCritic

def run_composition_pipeline(mood: str, region: str):
    """Initializes Muse-AI for neural music composition and aesthetic analysis."""
    print(f"--- Muse-AI: Starting Neural Composition for {region} ({mood}) ---")
    composer = NeuralComposer(model="muse-v1-production", base_scale="Harmonic-Lydian")
    critic = AestheticCritic(sensitivity=0.92)
    
    # 1. Setting parameters
    composer.set_cultural_parameters(mood, region)
    
    # 2. Composing melody
    melody = composer.generate_melody(bars=4)
    print(f"Neural Melody Synthesized: {melody}")
    
    # 3. Generating harmony
    chords = composer.synthesize_chords(melody)
    print(f"Harmonic Progression Found: {chords}")
    
    # 4. Neural Evaluation
    evaluation = critic.evaluate_melody(melody)
    print(f"Aesthetic Score: {evaluation['total_resonance']} ({evaluation['critique']})")
    
    # 5. Piece Analysis
    mood_match = critic.analyze_mood_alignment(melody, mood)
    print(f"Mood Alignment Confidence: {round(mood_match * 100, 2)}%")

def main():
    parser = argparse.ArgumentParser(description="Muse-AI: Generative Neural Music & Cultural Synthesis")
    parser.add_argument("--mode", type=str, choices=["compose", "analyze"], default="compose",
                        help="Execution mode for the Muse Engine.")
    parser.add_argument("--mood", type=str, default="Meditation",
                        help="The emotional target for neural synthesis.")
    parser.add_argument("--region", type=str, default="Indo-Ambient",
                        help="The cultural context for harmonic scale mapping.")
    
    args = parser.parse_args()
    
    if args.mode == "compose":
        run_composition_pipeline(args.mood, args.region)
    else:
        print(f"Error: Visual Aesthetic Mapping Mode ({args.mode}) is currently undergoing neural training.")

if __name__ == "__main__":
    main()