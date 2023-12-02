import { toRefs, reactive ,watchEffect } from "vue";

export default function(url, options){
    
    const state= reactive({
        response: [],
        error: null,
        fetching: true
    })

    const fetchData= async ()=>{

        try {
           const res= await fetch(url, options);
            const json= await res.json()
            state.response= json
            console.log(state.response)
        } catch (errors) {
            state.error= errors
        }finally{
            state.fetching= false;
        }
    }
    watchEffect(()=>{
        fetchData()
    })
    return { ...toRefs(state)};
}

