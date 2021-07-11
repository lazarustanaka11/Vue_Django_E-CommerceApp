<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title"> Thank You!</h1>
                <p>Your Order will be shipped within the next 72 hours!!</p>
            </div>

        </div>
    </div>
    
</template>
<script>
export default {
    name: 'Success',
    mounted(){
        document.title= 'Success | ZimboShop'
    },  
}
</script>