document.addEventListener('DOMContentLoaded', function () {
    const link = document.getElementById('follow');
    const follower_text = document.getElementById('followers_text');
    const followers_number = document.getElementById('followers_number');
    const following_number = document.getElementById('following_number')
    const title = document.title;

    if( link && title === 'Notifications'){
        link.addEventListener('click', function(event) {
            event.preventDefault();

            const dataId = link.getAttribute('data-id');
            const dataAction = link.getAttribute('data-action');

            const data = {
                id: dataId,
                action: dataAction
            };

            fetch('/profile/follow/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify(data)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log('else if')
                let newNumber = parseInt(following_number.textContent, 10);
                if (dataAction === 'follow') {
                    link.remove();
                    document.getElementById('div_follow').remove();
                    newNumber += 1;
                    updateElementById('following_number', newNumber);
                    link.setAttribute('data-action', 'unfollow');
                } else {
                    newNumber -= 1;
                    updateElementById('following_number', newNumber);
                    link.setAttribute('data-action', 'follow');
                }

            })
            .catch(error => {
                console.error('Fetch error:', error);
            });
        })
    }
    
    else if (link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();

            const dataId = link.getAttribute('data-id');
            const dataAction = link.getAttribute('data-action');

            const data = {
                id: dataId,
                action: dataAction
            };

            fetch('/profile/follow/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify(data)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                let newNumber = parseInt(followers_number.textContent, 10);
                if (dataAction === 'follow') {
                    updateElementById('follow', 'Unfollow');
                    newNumber += 1;
                    updateElementById('followers_number', newNumber);
                    link.setAttribute('data-action', 'unfollow');
                } else {
                    updateElementById('follow', 'Follow');
                    newNumber -= 1;
                    updateElementById('followers_number', newNumber);
                    link.setAttribute('data-action', 'follow');
                }
                updateElementById('followers_text', newNumber > 1 ? 'Followers' : 'Follower');

            })
            .catch(error => {
                console.error('Fetch error:', error);
            });
        });
    
    

    }

    function updateElementById(elementId, newTextContent) {
        const element = document.getElementById(elementId);

        if (element) {
            element.textContent = newTextContent;
        } else {
            console.error(`Element with ID "${elementId}" not found.`);
        }
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
