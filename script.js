// script.js

fetch('data_base.json')
    .then(response => response.json())
    .then(data => {
        displayProfile(data.profile);
        displaySkills(data.skills);
        displayHobbies(data.hobbies);
        displayExperience(data.experience);
        displayEducation(data.education);
        displayAwards(data.awards);
    })
    .catch(error => console.error('Erreur lors du chargement du CV:', error));

function displayProfile(profile) {
    document.getElementById('full-name').textContent = profile.firstName + ' ' + profile.lastName;
    document.getElementById('address').textContent = profile.address;
    document.getElementById('phone').textContent = profile.phone;
    document.getElementById('email').textContent = profile.email;
    document.getElementById('github').textContent = profile.github;
}

function displaySkills(skills) {
    const skillsList = document.getElementById('skills-list');
    const programmingSkills = skills.programming.map(skill => `<li>${skill}</li>`).join('');
    const cybersecuritySkills = skills.cybersecurity.map(skill => `<li>${skill}</li>`).join('');
    skillsList.innerHTML = `<strong>Programmation :</strong>${programmingSkills}<br><strong>Cybersécurité :</strong>${cybersecuritySkills}`;
}

function displayHobbies(hobbies) {
    const hobbiesList = document.getElementById('hobbies-list');
    hobbies.forEach(hobby => {
        const li = document.createElement('li');
        li.textContent = hobby;
        hobbiesList.appendChild(li);
    });
}

function displayExperience(experience) {
    const experienceList = document.getElementById('experience-list');
    experience.forEach(job => {
        const div = document.createElement('div');
        div.classList.add('job');
        div.innerHTML = `
            <h3>${job.title} | ${job.company || ''}</h3>
            <span>${job.dates} - ${job.position}</span>
        `;
        experienceList.appendChild(div);
    });
}

function displayEducation(education) {
    const educationList = document.getElementById('education-list');
    education.forEach(edu => {
        const div = document.createElement('div');
        div.classList.add('degree');
        div.innerHTML = `
            <h3>${edu.program}</h3>
            <p>${edu.institution}</p>
        `;
        educationList.appendChild(div);
    });
}

function displayAwards(awards) {
    const awardsList = document.getElementById('awards-list');
    awards.forEach(award => {
        const li = document.createElement('li');
        li.textContent = award;
        awardsList.appendChild(li);
    });
}
