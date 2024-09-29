<script>
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function() {
            const bookId = this.getAttribute('data-id');
            fetch(`/cart/add/${bookId}/`, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                }
            })
            .then(response => response.json())
            .then(data => {
                // Обновление количества товаров в корзине и скрытие кнопки
                document.querySelector('.cart-count').innerText = data.cart_length;
                this.style.display = 'none'; // Скрыть кнопку
            });
        });
    });
</script>
