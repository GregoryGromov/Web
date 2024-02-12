<template>
    <main class=" container text-white">
        <div class="h-56 grid grid-cols-3 gap-4 content-start px-8 py-4">

            <div>
                <label for="first_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                    Type
                </label>

                <select v-model="selected"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                    <option disabled value="">Selet type</option>
                    <option v-for="type in typesOfEquipment">
                        {{ type.name }}
                    </option>
                </select>
            </div>



            <div v-if="selected">

                <div class="grid gap-6 mb-6 md:grid-cols-2"
                    v-for="feature in typesOfEquipment.find(equipment => equipment.name === selected).features">
                    <!-- <p>{{ feature.name }}</p>
                
                <input v-model="feature.value" :placeholder="feature.name" class="text-black"> -->
                    <form>
                        <label for="first_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            {{ feature.name }}
                        </label>
                        <input v-model="feature.value" type="text" id="first_name"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            :placeholder="feature.name">
                    </form>
                </div>


            </div>


            <!-- <button @click="addEquipment" class="bg-red-300 text-black">Добавить</button> -->
        </div>

        <button type="button"
            class=" my1 mx-8 px-12 py-4 text-white bg-teal-700 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
            @click="addEquipment">
            Добавить
        </button>


        <div v-if="addedEquipment.length > 0" class="pt-8">
            <div 
                v-for="equipment in addedEquipment" 
                :key="equipment.id"
                class="my-4 mx-6 bg-teal-900 rounded-2xl px-8 py-4"
            >
                <h2 class="text-white pb-2">{{ equipment.name }}</h2>
                <div>
                    <p class="text-gray-400 pl-8" v-for="feature in equipment.features">
                        {{ feature.name }}: {{ feature.value }}
                    </p>
                </div>
            </div>
            <button type="button"
                class=" my1 mx-6 px-12 py-4 text-white bg-teal-700 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
                @click="sendEquipment">
                Отправить
            </button>
        </div>


        <p> {{text}}</p>



    </main>
</template>
  
<script setup>
import { ref } from "vue";
import { v4 as uuidv4 } from 'uuid';

const selected = ref("");
const text = ref("");

const addEquipment = () => {
    // console.log(typesOfEquipment.find(equipment => equipment.name === selected))

    console.log(typesOfEquipment.value.find(equipment => equipment.name === selected.value))
    const selectedEquipment = typesOfEquipment.value.find(equipment => equipment.name === selected.value)
    selectedEquipment.id = uuidv4();
    addedEquipment.value.push(selectedEquipment)
    console.log(addedEquipment.value)
    typesOfEquipment.value = typesOfEquipmentEtalon.value
    //selected.value = ""
}


const sendEquipment = () => {
    for (let element of addedEquipment.value) {
        let requestString = 'POST/HTTP/1.1/'
        requestString += `"${element.name}"_where_features:`
        for (let feature of element.features) {
            requestString += `name="${feature.name}"&value="${feature.value}"`
        }
        console.log(requestString);
        alert(`Отправлен запрос ${requestString}`)  
    }

    addedEquipment.value = []
}


const queryPost = ref("")

const typesOfEquipmentEtalon = ref([
    {
        name: "Computer",
        features: [
            { name: 'Memory', value: '' },
            { name: 'CPU', value: '' },
            { name: 'Video card', value: '' },
        ]
    },
    {
        name: "Thermometer",
        features: [
            { name: 'Max value', value: '' },
        ]
    }
])

const typesOfEquipment = ref([
    {
        name: "Computer",
        features: [
            { name: 'Memory', value: '' },
            { name: 'CPU', value: '' },
            { name: 'Video card', value: '' },
        ]
    },
    {
        name: "Thermometer",
        features: [
            { name: 'Max value', value: '' },
        ]
    }
])

const addedEquipment = ref([]);



</script>