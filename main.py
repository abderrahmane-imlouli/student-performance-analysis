import pandas as pd
import matplotlib.pyplot as plt
import os

def CreateDF():
    data = {
        "Name": ["ahmed", "Karim", "abderrahmane", "amine", "khaled"],
        "Math": [14, 9, 18, 12, 16],
        "Science": [16, 11, 17, 13, 15],
        "English": [13, 10, 19, 14, 12]
    }
    students = pd.DataFrame(data)
    return students

def ExploreDF(students):
    print("=== Task 1: Explore ===")
    print("Shape:", students.shape)     # (5,4)
    print("Columns:", list(students.columns))
    print("\nFirst 3 rows:")
    print(students.head(3).to_string(index=False))

    # calcualte the avg
    students["Average"] = students[["Math", "Science", "English"]].mean(axis=1).round(2)
    print("\nDataFrame after adding 'Average':")
    print(students.to_string(index=False))
    print("\nStudents with Average >= 12:")
    print(students[students["Average"] >= 12].to_string(index=False))

    return students

def Stats(students):
    print("\n=== Task 2: Conditional Selection & Statistics ===")
    print("\nStudents with Science > 15 (Name & Average):")
    print(students[students["Science"] > 15][["Name", "Average"]].to_string(index=False))

    # Math statistic
    math_mean = students["Math"].mean()
    math_min = students["Math"].min()
    math_max = students["Math"].max()
    print("\nMath stats:")
    print(f"Mean = {math_mean:.2f}, Min = {math_min}, Max = {math_max}")

    # sorted DF by avg in descending order
    students_sorted = students.sort_values(by="Average", ascending=False).reset_index(drop=True)
    print("\nStudents sorted by Average (desc):")
    print(students_sorted.to_string(index=False))

    return students_sorted

def DFCombination(students):
    print("\n=== Task 3: Combining DataFrames ===")
    # activities DF
    activities = pd.DataFrame({
        "Name": ["ahmed", "Karim", "abderrahmane", "amine", "khaled"],
        "Club": ["Robotics", "Music", "Sports", "Robotics", "Music"]
    })
    # concatination
    merged_concat = pd.concat([students.reset_index(drop=True), activities["Club"].reset_index(drop=True)], axis=1)
    print("\nMerged with pd.concat(axis=1):")
    print(merged_concat.to_string(index=False))

    return merged_concat

def AVGBarChart(students, out_path="average_scores.png"):
    print(f"\nSaving bar chart to {out_path} ...")
    plt.figure(figsize=(8,5))
    plt.bar(students["Name"], students["Average"])
    plt.xlabel("Student Name")
    plt.ylabel("Average Score")
    plt.title("Average Scores by Student")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def LinePlot(students, out_path="math_vs_science.png"):
    print(f"Saving line plot to {out_path} ...")
    plt.figure(figsize=(8,5))
    plt.plot(students["Name"], students["Math"], label="Math", linestyle='-', marker='o')
    plt.plot(students["Name"], students["Science"], label="Science", linestyle='--', marker='s')
    plt.xlabel("Student Name")
    plt.ylabel("Score")
    plt.title("Math vs Science Scores")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def ScatterPlot(students, out_path="english_vs_average.png"):
    print(f"Saving scatter plot to {out_path} ...")
    plt.figure(figsize=(8,5))
    plt.scatter(students["English"], students["Average"], marker='D', s=80)
    plt.xlabel("English Score")
    plt.ylabel("Average Score")
    plt.title("English vs Average")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def main():
    os.makedirs("outputs", exist_ok=True)

    students = CreateDF()
    students = ExploreDF(students)
    students_sorted = Stats(students)
    merged_concat = DFCombination(students)

    students.to_csv("outputs/students.csv", index=False)
    merged_concat.to_csv("outputs/merged_concat.csv", index=False)

    AVGBarChart(students, out_path="outputs/average_scores.png")
    LinePlot(students, out_path="outputs/math_vs_science.png")
    ScatterPlot(students, out_path="outputs/english_vs_average.png")

    print("\n=== excution ends ===")
    print("files are savers in -> outputs/:")
    for f in os.listdir("outputs"):
        print("-", os.path.join("outputs", f))

if __name__ == "__main__":
    main()
