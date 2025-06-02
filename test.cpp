#include <iostream>
#include <vector>
#include <string>

void printCombination(const std::vector<std::string>& combination) {
    std::cout << "{";
    for (size_t i = 0; i < combination.size(); ++i) {
        std::cout << "\"" << combination[i] << "\"";
        if (i < combination.size() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "}" << std::endl;
}

void generateCombinations(const std::vector<std::string>& directors, int K, int start, std::vector<std::string>& currentCombination) {
    if (currentCombination.size() == K) {
        printCombination(currentCombination);
        return;
    }

    for (int i = start; i < directors.size(); ++i) {
        currentCombination.push_back(directors[i]);
        generateCombinations(directors, K, i + 1, currentCombination);
        currentCombination.pop_back();
    }
}

void generate(const char *directors[], int N, int K) {
    std::vector<std::string> directorsVector(directors, directors + N);
    std::vector<std::string> currentCombination;
    generateCombinations(directorsVector, K, 0, currentCombination);
}

int main() {
    const char *directors[] = {"Tom", "John", "Rose"};
    int N = 3;
    int K = 2;
    generate(directors, N, K);
    return 0;
}
