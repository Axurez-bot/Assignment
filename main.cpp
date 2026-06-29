#include <iostream>
#include <string>

using namespace std;

/**
 * Assignment Part 2: Interactive Recommendation Program
 * Topic: AI Content Generation Platforms (Disruptive Innovation Model)
 * Description: Recommends custom system prompt templates based on 
 * user-selected tasks and desired tones.
 */
void generateAIPersona(int taskChoice, int toneChoice) {
    cout << "\n======================================================\n";
    cout << "             GENERATED AI SYSTEM PROMPT                \n";
    cout << "======================================================\n";

    // Core conditional processing logic (Nested If/Else)
    if (taskChoice == 1) { // Software Engineering / Programming Task
        if (toneChoice == 1) {
            cout << "Persona: Senior Software Architect (Direct & Strict)\n\n";
            cout << "Prompt Template:\n";
            cout << "\"Act as an expert C++ developer. Review the following code \n";
            cout << "for optimizations, safety patterns, and memory leaks. Provide \n";
            cout << "only clean, refactored code and concise technical bullet points. \n";
            cout << "Do not include any introductory or conversational filler.\"\n";
        } else {
            cout << "Persona: Patient Code Tutor (Encouraging & Explanatory)\n\n";
            cout << "Prompt Template:\n";
            cout << "\"Act as a friendly computer science mentor. Analyze the logic \n";
            cout << "errors in this script step-by-step. Use clear analogies suitable \n";
            cout << "for a beginner student, and provide helpful hints rather than \n";
            cout << "giving away the direct answers immediately.\"\n";
        }
    } else if (taskChoice == 2) { // Creative Copywriting / Content Creation Task
        if (toneChoice == 1) {
            cout << "Persona: Professional Copywriter (Formal & Persuasive)\n\n";
            cout << "Prompt Template:\n";
            cout << "\"Act as a corporate marketing director. Write a high-converting \n";
            cout << "product launch announcement based on these technical specs. Use \n";
            cout << "sophisticated language, maintain a premium brand voice, and \n";
            cout << "ensure the structure ends with a highly compelling Call to Action.\"\n";
        } else {
            cout << "Persona: Viral Content Creator (Casual & Witty)\n\n";
            cout << "Prompt Template:\n";
            cout << "\"Act as a humorous tech influencer. Write an engaging social media \n";
            cout << "thread breaking down this technical concept. Use casual language, \n";
            cout << "modern tech slang, and relatable real-world analogies to maximize \n";
            cout << "audience engagement and shares.\"\n";
        }
    } else {
        cout << "[System Error]: Invalid selection matrix detected.\n";
    }
    cout << "======================================================\n";
}

int main() {
    int task = 0;
    int tone = 0;

    cout << "--- Local AI Prompt & Persona Recommendation Assistant ---\n\n";
    
    // 1. Task Choice Selection
    cout << "Select the type of objective you want the AI to perform:\n";
    cout << "1) Software Engineering / Programming Analysis\n";
    cout << "2) Creative Copywriting / Content Creation\n";
    cout << "Enter choice (1-2): ";
    cin >> task;

    // Robust Input Validation for Task Selection
    if (task < 1 || task > 2) {
        cout << "\n[Invalid Input] Processing halted. Please restart and select options 1 or 2.\n";
        return 0; // Graceful termination
    }

    // 2. Tone/Mood Choice Selection
    cout << "\nSelect the desired Persona Tone / Interaction Style:\n";
    cout << "1) Professional / Direct & Concise\n";
    cout << "2) Casual / Explanatory & Engaging\n";
    cout << "Enter choice (1-2): ";
    cin >> tone;

    // Robust Input Validation for Tone Selection
    if (tone < 1 || tone > 2) {
        cout << "\n[Invalid Input] Processing halted. Please restart and select options 1 or 2.\n";
        return 0; // Graceful termination
    }

    // Process sanitized inputs and deliver prompt recommendation
    generateAIPersona(task, tone);

    return 0;
}