import config from "@/config.js";
import { ref, reactive} from 'vue'

async function getLoginPost (identification, password){
    const settings = reactive({
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        identification: identification,
        password: password
    }),
    })
    const data = ref(null)
    const error = ref(null)
    await fetch(`${config.login_Path}/get_login/Authenticated`, settings)
    return response.json()
            
}
export default getLoginPost