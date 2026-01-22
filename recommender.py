def recommend_learning(missing_skills):
    recommendations = {}

    for skill in missing_skills:
        if skill in ["python", "java"]:
            recommendations[skill] = "Practice coding problems and build small projects"
        elif skill in ["machine learning", "deep learning"]:
            recommendations[skill] = "Learn core ML algorithms and implement them using scikit-learn"
        elif skill in ["sql"]:
            recommendations[skill] = "Practice SQL queries on real datasets"
        elif skill in ["power bi", "tableau"]:
            recommendations[skill] = "Build dashboards using sample datasets"
        elif skill in ["tensorflow", "pytorch"]:
            recommendations[skill] = "Implement basic neural networks and CNNs"
        elif skill in ["git", "github"]:
            recommendations[skill] = "Use Git daily for version control and collaboration"
        else:
            recommendations[skill] = "Learn fundamentals and apply in a mini project"

    return recommendations
