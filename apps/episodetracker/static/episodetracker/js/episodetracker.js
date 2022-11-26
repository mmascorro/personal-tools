


let episodeData = {}

const container = document.getElementById('container');
const seriesNameInput = document.getElementById('series');
const addSeriesBtn = document.getElementById('addSeries');
const csrftoken = document.querySelector('input[name=csrfmiddlewaretoken]').value;

addSeriesBtn.addEventListener('click', e => {

  let formData = new FormData();
  formData.append('name', seriesNameInput.value.trim());

  let options = {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrftoken
    },
    credentials: 'same-origin',
    body: formData
  }

  fetch('/episodetracker/shows/', options)
  .then(response => response.json())
  .then(data => {
    seriesNameInput.value = '';
    loadData();
  });


})

async function saveData(show, episode, action) {

  let formData = new FormData();
  formData.append('show', show);
  formData.append('episode', episode);
  formData.append('action', action);


  let options = {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrftoken
    },
    credentials: 'same-origin',
    body: formData
  }

  fetch(`/episodetracker/shows/${show}`, options)
  .then(response => response.json())
  .then(data => {    
    loadData()
  });

}

async function loadData() {
  let options = {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  }

  let response = await fetch('/episodetracker/shows/', options);

  if (response.ok) {
    let data = await response.json();
    episodeData = data;
  }

  buildUI();


}

async function buildUI() {
  container.replaceChildren()
  episodeData.forEach( (show, index)=> {

    let holdTimer;

    let showContainer = document.createElement('div');
    showContainer.classList.add('showContainer');
    showContainer.dataset.show = show.id;
    showContainer.dataset.episode = show.episode;
    
    let showTitle = document.createElement('p');
    showTitle.innerHTML = show.name;
    showContainer.appendChild(showTitle);

    let showEpisode = document.createElement('p');
    showEpisode.classList.add('episodeNumber')
    showEpisode.innerHTML = show.episode;
    showContainer.appendChild(showEpisode);

    let episodeCountDown = document.createElement('button');
    episodeCountDown.innerHTML = '-';
    episodeCountDown.classList.add('count');
    episodeCountDown.addEventListener('click', e => {
      showContainer.dataset.episode--;
      saveData(show=showContainer.dataset.show, episode=showContainer.dataset.episode, action='update');
    })
    showContainer.appendChild(episodeCountDown);
    
    let episodeCountUp = document.createElement('button');
    episodeCountUp.innerHTML = '+';
    episodeCountUp.classList.add('count');
    episodeCountUp.addEventListener('click', e => {
      showContainer.dataset.episode++
      saveData(show=showContainer.dataset.show, episode=showContainer.dataset.episode, action='update');
    })
    showContainer.appendChild(episodeCountUp);


    let removeShowBtn = document.createElement('button');
    removeShowBtn.innerHTML = 'X';
    removeShowBtn.classList.add('remove');
    removeShowBtn.addEventListener('click', e => {
      saveData(show=showContainer.dataset.show, episode=showContainer.dataset.episode, action='delete');
    });
    showContainer.appendChild(removeShowBtn);

    showContainer.addEventListener('touchstart', e => {
      holdTimer = setTimeout(() => {
        showContainer.classList.toggle('hold');
      }, 1000);
    });
    showContainer.addEventListener('mousedown', e => {
      holdTimer = setTimeout(() => {
        showContainer.classList.toggle('hold');
      }, 1000);
    });

    showContainer.addEventListener('touchend', e => {
      clearTimeout(holdTimer)
    });
    showContainer.addEventListener('mouseup', e => {
      clearTimeout(holdTimer)
    });

    container.appendChild(showContainer);
  });


}


//start
loadData();