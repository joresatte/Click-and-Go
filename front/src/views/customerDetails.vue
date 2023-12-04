<template>
    <div>
        <div>
            {{ receipt }}
        </div>
        <div>
            {{ startUp }}
        </div>
        <div>
            {{ text }}
        </div>
    </div>
</template>
<script setup>
import { ref, onMounted } from 'vue';
const receipt= ref('Comprobante de la entrega')
const startUp= ref('test/Online')
const text= ref('Contigo')
const props = defineProps(['id'])
onMounted(()=> {
    loadData()
    if(window.localStorage){
        if(localStorage.getItem('pathId')!== undefined && localStorage.getItem('pathId') ){
            router.push({
                path: `/client/:id`,
                name: 'customerDetails',
                params:{id: e}
                })
        }else{
            return
        }
    }
})
</script>
<style scoped>
</style>