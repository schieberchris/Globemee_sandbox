import streamlit as st
import matplotlib.pyplot as plt

# Sprachniveau-Rangfolge
language_levels = {"A1": 1, "A2": 2, "B1": 3, "B2": 4, "C1": 5, "C2": 6}

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
        "language": {"type": "Deutsch", "level": "B2"},
        "max_salary": 45000,
        "travel_willingness": "hoch"
    },
    {
        "id": 2,
        "title": "Industrieelektriker",
        "required_skills": [
            {"skill_id": 1, "importance": 4},
            {"skill_id": 2, "importance": 5},
            {"skill_id": 3, "importance": 5},
            {"skill_id": 8, "importance": 4}
        ],
        "language": {"type": "Englisch", "level": "B1"},
        "max_salary": 48000,
        "travel_willingness": "mittel"
    },
    {
        "id": 3,
        "title": "Elektroniker für Gebäudetechnik",
        "required_skills": [
            {"skill_id": 1, "importance": 5},
            {"skill_id": 4, "importance": 5},
            {"skill_id": 5, "importance": 3},
            {"skill_id": 7, "importance": 3}
        ],
        "language": {"type": "Deutsch", "level": "B1"},
        "max_salary": 42000,
        "travel_willingness": "mittel"
    },
    {
        "id": 4,
        "title": "Servicetechniker für erneuerbare Energien",
        "required_skills": [
            {"skill_id": 10, "importance": 5},
            {"skill_id": 1, "importance": 4},
            {"skill_id": 9, "importance": 4},
            {"skill_id": 4, "importance": 3}
        ],
        "language": {"type": "Deutsch", "level": "B2"},
        "max_salary": 47000,
        "travel_willingness": "hoch"
    },
    {
        "id": 5,
        "title": "Prüftechniker",
        "required_skills": [
            {"skill_id": 5, "importance": 5},
            {"skill_id": 9, "importance": 5},
            {"skill_id": 1, "importance": 4},
            {"skill_id": 3, "importance": 3}
        ],
        "language": {"type": "Englisch", "level": "B2"},
        "max_salary": 46000,
        "travel_willingness": "mittel"
    },
    {
        "id": 6,
        "title": "SPS-Programmierer",
        "required_skills": [
            {"skill_id": 8, "importance": 5},
            {"skill_id": 7, "importance": 4},
            {"skill_id": 9, "importance": 3}
        ],
        "language": {"type": "Englisch", "level": "C1"},
        "max_salary": 50000,
        "travel_willingness": "hoch"
    }
]

# Bewerberdaten
applicants = [
   {
      "id": 1,
      "name": "Luis Garcia",
      "skills": [1, 3, 5],
      "language": {"type": "Deutsch", "level": "B2"},
      "salary_expectation": 44000,
      "travel_willingness": "hoch"
    },
    {
      "id": 2,
      "name": "Maria Fernandez",
      "skills": [2, 4, 10],
      "language": {"type": "Spanisch", "level": "C2"},
      "salary_expectation": 46000,
      "travel_willingness": "mittel"
    },
    {
      "id": 3,
      "name": "Carlos Martinez",
      "skills": [1, 7, 8],
      "language": {"type": "Englisch", "level": "B1"},
      "salary_expectation": 45000,
      "travel_willingness": "hoch"
    },
    {
      "id": 4,
      "name": "Ana Lopez",
      "skills": [4, 6, 9],
      "language": {"type": "Deutsch", "level": "A2"},
      "salary_expectation": 42000,
      "travel_willingness": "mittel"
    },
    {
      "id": 5,
      "name": "Juan Gonzalez",
      "skills": [2, 3, 10],
      "language": {"type": "Spanisch", "level": "B1"},
      "salary_expectation": 47000,
      "travel_willingness": "hoch"
    },
    {
      "id": 6,
      "name": "Isabella Ramirez",
      "skills": [1, 4, 8],
      "language": {"type": "Deutsch", "level": "C1"},
      "salary_expectation": 46000,
      "travel_willingness": "hoch"
    },
    {
      "id": 7,
      "name": "Pedro Sanchez",
      "skills": [5, 6, 7],
      "language": {"type": "Englisch", "level": "B2"},
      "salary_expectation": 44000,
      "travel_willingness": "mittel"
    },
    {
      "id": 8,
      "name": "Lucia Martinez",
      "skills": [3, 7, 10],
      "language": {"type": "Spanisch", "level": "C2"},
      "salary_expectation": 45000,
      "travel_willingness": "hoch"
    },
    {
      "id": 9,
      "name": "Javier Morales",
      "skills": [1, 2, 5],
      "language": {"type": "Deutsch", "level": "B2"},
      "salary_expectation": 43000,
      "travel_willingness": "hoch"
    },
    {
      "id": 10,
      "name": "Elena Vega",
      "skills": [4, 8, 9],
      "language": {"type": "Englisch", "level": "A1"},
      "salary_expectation": 40000,
      "travel_willingness": "mittel"
    },
    {
      "id": 11,
      "name": "Diego Cruz",
      "skills": [2, 6, 8],
      "language": {"type": "Spanisch", "level": "B1"},
      "salary_expectation": 48000,
      "travel_willingness": "hoch"
    },
    {
      "id": 12,
      "name": "Victoria Ruiz",
      "skills": [1, 5, 7],
      "language": {"type": "Deutsch", "level": "B2"},
      "salary_expectation": 45000,
      "travel_willingness": "hoch"
    },
    {
      "id": 13,
      "name": "Rafael Ortega",
      "skills": [3, 6, 9],
      "language": {"type": "Spanisch", "level": "C1"},
      "salary_expectation": 46000,
      "travel_willingness": "mittel"
    },
    {
      "id": 14,
      "name": "Carmen Torres",
      "skills": [1, 4, 10],
      "language": {"type": "Englisch", "level": "B2"},
      "salary_expectation": 44000,
      "travel_willingness": "hoch"
    },
    {
      "id": 15,
      "name": "Adrian Castillo",
      "skills": [2, 3, 5],
      "language": {"type": "Deutsch", "level": "C2"},
      "salary_expectation": 47000,
      "travel_willingness": "hoch"
    },
    {
      "id": 16,
      "name": "Gabriela Reyes",
      "skills": [4, 6, 8],
      "language": {"type": "Spanisch", "level": "B2"},
      "salary_expectation": 43000,
      "travel_willingness": "mittel"
    },
    {
      "id": 17,
      "name": "Fernando Alvarez",
      "skills": [1, 2, 7],
      "language": {"type": "Englisch", "level": "A2"},
      "salary_expectation": 45000,
      "travel_willingness": "hoch"
    },
    {
      "id": 18,
      "name": "Sara Mendoza",
      "skills": [3, 9, 10],
      "language": {"type": "Deutsch", "level": "B1"},
      "salary_expectation": 42000,
      "travel_willingness": "mittel"
    },
    {
      "id": 19,
      "name": "Manuel Ortiz",
      "skills": [5, 6, 8],
      "language": {"type": "Spanisch", "level": "C1"},
      "salary_expectation": 46000,
      "travel_willingness": "hoch"
    },
    {
      "id": 20,
      "name": "Sofia Navarro",
      "skills": [2, 4, 7],
      "language": {"type": "Englisch", "level": "C2"},
      "salary_expectation": 47000,
      "travel_willingness": "hoch"
    }
]

# Funktion zur Berechnung des Scores
def calculate_score(applicant, job):
    score = 0
    for skill in job["required_skills"]:
        if skill["skill_id"] in applicant["skills"]:
            score += skill["importance"] * 2
    if applicant["language"]["type"] == job["language"]["type"] and language_levels[applicant["language"]["level"]] >= language_levels[job["language"]["level"]]:
        score += 10
    if applicant["salary_expectation"] <= job["max_salary"]:
        score += 15
    else:
        score -= 5 * ((applicant["salary_expectation"] - job["max_salary"]) // 1000)
    if applicant["travel_willingness"] == job["travel_willingness"]:
        score += 5
    return score

# Mapping und Scoring
def map_and_score_applicants(applicants, jobs):
    mapping_with_scores = []
    for job in jobs:
        job_matches = {"job_title": job["title"], "applicants": []}
        for applicant in applicants:
            score = calculate_score(applicant, job)
            job_matches["applicants"].append({
                "name": applicant["name"],
                "skills": [skill["name"] for skill in skill_model["skills"] if skill["id"] in applicant["skills"]],
                "language": f"{applicant['language']['type']} ({applicant['language']['level']})",
                "salary_expectation": applicant["salary_expectation"],
                "travel_willingness": applicant["travel_willingness"],
                "score": score
            })
        mapping_with_scores.append(job_matches)
    return mapping_with_scores

# Mapping und Scoring
mapping_with_scores = map_and_score_applicants(applicants, job_requirements)

# Streamlit UI
st.title("Job-Matching mit interaktiven Filtern und Diagrammen")

# Filter: Job auswählen
job_titles = [job["title"] for job in job_requirements]
selected_job_title = st.selectbox("Wähle einen Job:", ["Alle Jobs"] + job_titles)

# Filter: Sprachniveau
languages = ["Alle", "Deutsch", "Englisch", "Spanisch"]
selected_language = st.selectbox("Filtere nach Sprache:", languages)
selected_language_level = st.select_slider("Filtere nach Sprachniveau:", options=["A1", "A2", "B1", "B2", "C1", "C2"])

# Filter: Skills
selected_skills = st.multiselect("Filtere nach Skills:", [skill["name"] for skill in skill_model["skills"]])

# Ergebnisse filtern und anzeigen
for job in mapping_with_scores:
    if selected_job_title != "Alle Jobs" and job["job_title"] != selected_job_title:
        continue

    st.subheader(f"Job: {job['job_title']}")
    scores = []
    names = []
    for applicant in job["applicants"]:
        if selected_language != "Alle" and applicant["language"].split(" ")[0] != selected_language:
            continue
        if language_levels[selected_language_level] > language_levels[applicant["language"].split(" ")[1].replace("(", "").replace(")", "")]:
            continue
        if selected_skills and not any(skill in applicant["skills"] for skill in selected_skills):
            continue
        st.write(f"**Bewerber:** {applicant['name']}")
        st.write(f"- Skills: {', '.join(applicant['skills'])}")
        st.write(f"- Sprache: {applicant['language']}")
        st.write(f"- Gehalt: {applicant['salary_expectation']} €")
        st.write(f"- Reisebereitschaft: {applicant['travel_willingness']}")
        st.write(f"- **Score:** {applicant['score']}")
        st.write("---")
        scores.append(applicant["score"])
        names.append(applicant["name"])
    
    # Diagramm
    if scores:
        fig, ax = plt.subplots()
        ax.barh(names, scores, color='skyblue')
        ax.set_xlabel("Score")
        ax.set_ylabel("Bewerber")
        ax.set_title(f"Scores für {job['job_title']}")
        st.pyplot(fig)