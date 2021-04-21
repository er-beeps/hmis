<template>
  <div>
    <base-template>
      <hello-world></hello-world>
    </base-template>
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import BaseTemplate from "./components/BaseTemplate.vue";

export default {
  components: {
    HelloWorld,
    BaseTemplate,
  },
};
</script>


<style>
</style>
