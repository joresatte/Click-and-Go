import config from "@/config.js";
import { ref, reactive} from 'vue'

async function getLoginPost (settings){
    const identify= ref(identificatioValue)
    const pass= ref(passwordValue)
    console.log(identify.value, pass.value)
    // const settings = reactive({
    // method: "POST",
    // headers: {
    //     "Content-Type": "application/json",
    // },
    // body: JSON.stringify({
    //     identification: identify.value,
    //     password: pass.value
    // }),
    // })
    const data = ref(null)
    const error = ref(null)
    await fetch(`${config.login_Path}/get_login/Authenticated`, settings)
            .then((res) => res.json())
            .then((json) => (data.value = json))
            .catch((err) => (error.value = err))
    return {data, error}
            
}
export default getLoginPost