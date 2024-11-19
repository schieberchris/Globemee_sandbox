import streamlit as st

# Skill-Datenmodell
skill_model = {
    "skills": [
        {"id": 1, "name": "230V-Anlagentechnik"},
        {"id": 2, "name": "Hochspannungstechnik"},
        {"id": 3, "name": "Schaltanlagenmontage"},
        {"id": 4, "name": "Elektroinstallation"},
        {"id": 5, "name": "Prüfung nach DGUV V3"},
        {"id": 6, "name": "Löttechnik"},
        {"id": 7, "name": "EDV-Kenntnisse"},
        {"id": 8, "name": "Steuerungstechnik (SPS)"},
        {"id": 9, "name": "Mess- und Prüftechnik"},
        {"id": 10, "name": "Erneuerbare Energien"}
    ]
}

# Job-Anforderungen
job_requirements = [
    {
        "id": 1,
        "title": "Betriebselektriker",
        "required_skills": [
            {"skill_id": 1, "importance": 5},
            {"skill_id": 3, "importance": 4},
            {"skill_id": 5, "importance": 4},
            {"skill_id": 9, "importance": 3}
        ],
        "language": "Deutsch",
        "max_salary": 45000,
        "travel_willingness": "hoch"
    }
]

# Bewerberdaten
applicants = [
    {
        "id": 1,
        "name": "Max Mustermann",
        "skills": [1, 3, 5],
        "language": "Deutsch",
        "salary_expectation": 45000,
        "travel_willingness": "hoch"
    },
    {
        "id": 2,
        "name": "Sarah Müller",
        "skills": [2, 3, 8],
        "language": "Englisch",
        "salary_expectation": 48000,
        "travel_willingness": "mittel"
    }
]

# Funktion zur Berechnung des Scores
def calculate_score(applicant, job):
    score = 0
    for skill in job["required_skills"]:
        if skill["skill_id"] in applicant["skills"]:
            score += skill["importance"] * 2  # Gewichtung
    if applicant["language"] == job["language"]:
        score += 10
    if applicant["salary_expectation"] <= job["max_salary"]:
        score += 15
    else:
        score -= 5 * ((applicant["salary_expectation"] - job["max_salary"]) // 1000)
    if applicant["travel_willingness"] == job["travel_willingness"]:
        score += 5
    return score

# Scoring und Mapping durchführen
def map_and_score_applicants(applicants, jobs):
    mapping_with_scores = []
    for job in jobs:
        job_matches = {"job_title": job["title"], "applicants": []}
        for applicant in applicants:
            score = calculate_score(applicant, job)
            job_matches["applicants"].append({
                "name": applicant["name"],
                "skills": [skill["name"] for skill in skill_model["skills"] if skill["id"] in applicant["skills"]],
                "language_match": applicant["language"] == job["language"],
                "salary_match": applicant["salary_expectation"] <= job["max_salary"],
                "travel_match": applicant["travel_willingness"] == job["travel_willingness"],
                "score": score
            })
        mapping_with_scores.append(job_matches)
    return mapping_with_scores

# Mapping und Scoring
mapping_with_scores = map_and_score_applicants(applicants, job_requirements)

# Streamlit UI
st.title("Job-Matching Visualisierung")
st.write("Dies ist eine Übersicht der Bewerber und ihrer Scores für verschiedene Jobs.")

for job in mapping_with_scores:
    st.subheader(f"Job: {job['job_title']}")
    for applicant in job["applicants"]:
        st.write(f"**Bewerber:** {applicant['name']}")
        st.write(f"- Skills: {', '.join(applicant['skills'])}")
        st.write(f"- Sprache passend: {applicant['language_match']}")
        st.write(f"- Gehalt passend: {applicant['salary_match']}")
        st.write(f"- Reisebereitschaft passend: {applicant['travel_match']}")
        st.write(f"- **Score:** {applicant['score']}")
        st.write("---")