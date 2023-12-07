<template>
    <div>
        <AppLogo/>
    </div>
    <div class="details">
        <info msg="Comprobante de la entrega"/>
    </div>
</template>
<script setup>
    import AppLogo from "@/components/appLogo.vue";
    import info from "@/components/info.vue";
</script>
<style scoped>
    @media (min-width: 1024px) {
        .login {
            min-height: 100vh;
            display: flex;
            align-items: center;
        }
    }
</style>