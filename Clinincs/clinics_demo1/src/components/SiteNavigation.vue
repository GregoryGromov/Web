<template>
    <header class="sticky top-0 bg-weather-primary shadow-lg">
        <nav class="container flex flex-col sm:flex-row items-center gap-4 text-white py-6">
            <RouterLink :to="{ name: 'list' }">
                <div class="px-16 flex items-center gap-3 ">
                    <i class="fa-solid fa-house-chimney-medical text-2xl"></i>
                    <p class="text-2xl">Clinic MatMeh</p>
                </div>
            </RouterLink>

            <div class="flex gap-10 flex-1 justify-end">
                <RouterLink :to="{ name: 'list' }">
                    <i class="text-xl hover:text-weather-secondary duration-150 cursor-pointer">
                        Список
                    </i>
                </RouterLink>

                <RouterLink :to="{ name: 'add' }">
                    <i class="text-xl hover:text-weather-secondary duration-150 cursor-pointer">
                        Добавление
                    </i>
                </RouterLink>

                <RouterLink :to="{ name: 'transactions' }">
                <i class="text-xl hover:text-weather-secondary duration-150 cursor-pointer">
                    Журнал операций
                </i>
                </RouterLink>


                <i @click="toggleModal"
                    class="fa-solid fa-address-card text-4xl hover:text-weather-secondary duration-150 cursor-pointer">

                </i>

            </div>

            <BaseModel :modalActive="modalActive" @close-modal="toggleModal">
                <h1 class="text-black"> Тут скоро добавится инфо </h1>
            </BaseModel>

        </nav>
    </header>
</template>

<script setup>
import { ref } from "vue";
import { RouterLink } from 'vue-router';
import BaseModel from './BaseModel.vue';

const modalActive = ref(null);
const toggleModal = () => {
    modalActive.value = !modalActive.value;
};

</script>
