document.addEventListener('DOMContentLoaded', function () {
    const checkoutButton = document.getElementById('rzp-button1');
    const checkoutData = document.getElementById("checkout-data");
    const email = checkoutData.getAttribute("data-email");
    const fullName = checkoutData.getAttribute("data-fullname");
    const totalItemAmount = document.getElementById("total_item_amount");

    function getCookie(name) {
        let value = "; " + document.cookie;
        let parts = value.split("; " + name + "=");
        if (parts.length === 2) return parts.pop().split(";").shift();
    }

    checkoutButton.addEventListener('click', function (event) {
        event.preventDefault();

        const rawPrice = totalItemAmount.textContent;
        const totalPrice = parseFloat(rawPrice.replace('₹', '').trim());

        fetch("http://127.0.0.1:3000/create-order/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                var options = {
                    "key": "rzp_test_sHE2W2x7qnm2Hh",
                    "amount": totalPrice * 100,
                    "currency": "INR",
                    "name": "Ecommerce",
                    "description": "Order Payment",
                    "order_id": data['order_id'],
                    "prefill": {
                        "name": fullName,
                        "email": email
                    },
                    "handler": function (response) {
                        const razorpay_order_id = response.razorpay_order_id;
                        const payment_id = response.razorpay_payment_id;
                        console.log(razorpay_order_id, payment_id)

                        fetch("http://127.0.0.1:3000/handle-payment/", {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                'X-CSRFToken': getCookie('csrftoken')
                            },
                            body: JSON.stringify({
                                'order_id': razorpay_order_id,
                                'payment_id': payment_id
                            })
                        })
                            .then(response => {
                                if (!response.ok) {
                                    throw new Error('Network response was not ok during payment handling');
                                }
                                return response.json();
                            })
                            .then(data => {
                                if (data.message === 'Payment successful') {
                                    const orderSection = document.getElementById('order-placed-section');
                                    const orderMessage = document.getElementById('order-success-message');

                                    orderMessage.textContent = "Successfully placed order!";
                                    orderSection.style.display = "block";
                                    // window.location.href = orderCompleteUrl + '?order_id=' + data.order_id + '&payment_id=' + data.transID;
                                    // console.log('Order ID:', data.order_id);
                                    // console.log('Payment ID:', data.transID);
                                
                                } else {
                                    alert('Payment failed');
                                }
                            })
                            .catch(error => {
                                 console.error('An error occurred while processing the payment.', error);
                                 alert('There was an issue processing your payment. Please try again.');
                             });
                    }
                };

                var rzp1 = new Razorpay(options);
                rzp1.open();
            })
            .catch(error => {
                console.error('Error creating order:', error);
                alert('There was an issue initiating your order. Please try again.');
            });
    });
});