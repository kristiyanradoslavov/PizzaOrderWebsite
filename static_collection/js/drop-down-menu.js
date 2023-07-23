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
    let price = document.getElementById('final-price');
    let currentQuantity = document.getElementById('current-quantity');
    let increaseQuantityBtn = document.getElementsByClassName('plus');
    let decreaseQuantityBtn = document.getElementsByClassName('minus');
    let smallImage = document.getElementsByClassName("small-img")[0];
    let largeImage = document.getElementsByClassName("large-img")[0];
    let selectedSize = null;

    let prices = {
        Small: document.getElementById('small'),
        Medium: document.getElementById('medium'),
        Large: document.getElementById('large'),
        ExtraLarge: document.getElementById('extra-large'),
        SinglePrice: document.getElementById('single')
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

    function sizeHandler(event) {
        let currentValue = event.target.value;
        let currentSelectedSize = currentValue.split(' ').join('');
        selectedSize = currentSelectedSize
        priceUpdate()

        if (smallImage && largeImage) {
            imageUpdate()
        }
    }

    function priceUpdate() {
        // debugger;
        let finalPrice = 0
        if (selectedSize) {
            let newPrice = Number(prices[selectedSize].textContent);
            finalPrice = newPrice * Number(currentQuantity.value);
        } else {
            let newPrice = price.textContent.trim().slice()
            finalPrice = Number(prices["SinglePrice"].textContent) * Number(currentQuantity.value);
        }
        price.textContent = `${finalPrice.toFixed(2)}€`;
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


    function increaseQuantity() {
        let quantityNum = Number(currentQuantity.value);
        quantityNum++;
        currentQuantity.value = quantityNum;
        priceUpdate();

    }

    function decreaseQuantity() {
        let quantityNum = Number(currentQuantity.value);
        if (quantityNum > 1) {
            quantityNum--;
        }
        currentQuantity.value = quantityNum;
        priceUpdate()
    }
}


dropDownEle()
calculateProductPrice()