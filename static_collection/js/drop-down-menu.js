function dropDownEle() {
    let dropElement = document.getElementsByClassName('drop-down-menu')[0]
    let profileBtn = document.getElementsByClassName('btn-wrapper')[0]

    window.addEventListener('click', eventHandler)

    function eventHandler(event) {
        let current_element = event.target

        if (current_element.closest('.btn-wrapper') === profileBtn) {
            changeDisplay(current_element)
        } else if (current_element != profileBtn && dropElement.style.display != 'none') {
            changeDisplay(current_element)
        }

    }

    function changeDisplay(current_element) {
        if (dropElement.style.display == 'block') {
            dropElement.style.display = "none"
        } else {
            if (current_element.closest('.btn-wrapper')) {
                dropElement.style.display = 'block'
            }
        }
    }
}

function calculateProductPrice() {
    let ele = document.getElementsByClassName('size-select');
    // let price = document.getElementsByClassName('final-price');
    // let currentQuantity = document.getElementById('current-quantity');
    let increaseQuantityBtn = document.getElementsByClassName('plus');
    let decreaseQuantityBtn = document.getElementsByClassName('minus');
    let smallImage = document.getElementsByClassName("small-img")[0];
    let largeImage = document.getElementsByClassName("large-img")[0];
    let selectedSize = null;
    let total_price = document.getElementById('total-price')
    let deleteItemBtn = document.getElementsByClassName('deleteItemBtn')


    let prices = {
        Small: document.getElementById('small'),
        Medium: document.getElementById('medium'),
        Large: document.getElementById('large'),
        ExtraLarge: document.getElementById('extra-large'),
        SinglePrice: document.getElementsByClassName('single')
    }

    for (let currentBtn of increaseQuantityBtn) {
        currentBtn.addEventListener('click', increaseQuantity)
    }

    for (let currentBtn of decreaseQuantityBtn) {
        currentBtn.addEventListener('click', decreaseQuantity);
    }

    for (let i = 0; i < ele.length; i++) {
        ele[i].addEventListener('click', sizeHandler);
    }

    for (const currentBtn of deleteItemBtn) {
        currentBtn.addEventListener('click', deleteHandler)
    }

    function deleteHandler(event) {
        if (event) {
            event.preventDefault();
        }
        let currentBtn = event.target.parentNode;

        let currentOrderIt = Number(currentBtn.getAttribute('data-item-id'))
        deleteCartItem(currentOrderIt)

    }

    function sizeHandler(event) {
        let currentValue = event.target.value;
        let currentSelectedSize = currentValue.split(' ').join('');
        selectedSize = currentSelectedSize
        priceUpdate(event)

        if (smallImage && largeImage) {
            imageUpdate()
        }
    }

    function priceUpdate(event) {
        let current_container = event.target.parentNode;
        let currentQuantity = current_container.querySelector('.current-quantity')
        let singlePrice = current_container.querySelector('.single')
        let price = null

        let finalPrice = 0
        if (selectedSize) {
            price = document.querySelector('.product-final-price')
            currentQuantity = document.getElementsByClassName('current-quantity')[0]
            let newPrice = Number(prices[selectedSize].textContent);
            finalPrice = newPrice * Number(currentQuantity.value);
        } else {
            finalPrice = Number(singlePrice.value) * Number(currentQuantity.value);
            price = current_container.parentNode.querySelector('.product-final-price')
        }

        price.textContent = `Price: ${finalPrice.toFixed(2)} €`

        if (total_price) {
            updateTotalPrice();
        }
    }

    function imageUpdate() {
        if (selectedSize === 'Small') {
            smallImage.classList = 'small-img'
            largeImage.classList = 'large-img hidden'
        } else if (selectedSize === 'Large') {
            smallImage.classList = 'small-img hidden'
            largeImage.classList = 'large-img'
        }
    }


    function increaseQuantity(event) {
        let current_container = event.target.parentNode;
        currentQuantity = current_container.querySelector('.current-quantity')

        let quantityNum = Number(currentQuantity.value);
        quantityNum++;
        let newQuantity = Number(quantityNum);
        let dbObjectId = Number(current_container.id)
        if (dbObjectId) {
            updateCartItemQuantity(dbObjectId, newQuantity)
        }

        currentQuantity.value = quantityNum;
        priceUpdate(event);

    }

    function decreaseQuantity(event) {
        let current_container = event.target.parentNode;
        currentQuantity = current_container.querySelector('.current-quantity')
        let dbObjectId = Number(current_container.id)
        let quantityNum = Number(currentQuantity.value);
        if (quantityNum > 1) {
            quantityNum--;
            let newQuantity = Number(quantityNum);

            if (dbObjectId) {
                updateCartItemQuantity(dbObjectId, newQuantity)
            }
        }
        currentQuantity.value = quantityNum;
        priceUpdate(event)
    }


    function updateTotalPrice() {
        let all_product_prices = Array.from(document.getElementsByClassName('product-final-price'))
        let new_total_price = 0
        for (const price of all_product_prices) {
            let stripedPrice = price.textContent.trim().split(" ")[1]
            new_total_price += Number(stripedPrice);
        }
        total_price.textContent = `Total Price: ${new_total_price.toFixed(2)}`;

    }

    function updateCartItemQuantity(itemId, newQuantity) {
        const formData = new FormData();
        formData.append('new_quantity', newQuantity);
        const csrfToken = getCookie('csrftoken');

        fetch(updateApiUrl.replace('0', itemId), {
            method: 'PUT',
            body: formData,
            headers: {
                'X-CSRFToken': csrfToken,
            },
        })
            .then(response => response.json())
            .then(data => {
                // Handle response or update the total price
            })
            .catch(error => {
                // Handle errors
                console.error('Error updating quantity:', error);
            });
    }

    async function deleteCartItem(itemId) {
        const csrfToken = getCookie('csrftoken');

        try {
            const response = await fetch(deleteApiUrl.replace('0', itemId), {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json',
                },
            })

            if (response.ok) {
                location.reload();
            } else {
                console.log("Error deleting item:", response.statusText)
            }
        } catch (error) {
            console.error('Error:', error);
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
}


dropDownEle()
calculateProductPrice()