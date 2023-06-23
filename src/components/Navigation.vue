<template>
    <div class="navigation">
      <router-link to="/comment" class="tab" :class="{ active: currentRoute === '/comment' }">Comment</router-link>
      <router-link to="/score" class="tab" :class="{ active: currentRoute === '/score' }">Score</router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Navigation',
    computed: {
      currentRoute() {
        return this.$route.path;
      }
    }
  };
  </script>
  
  <style>
  .navigation {
    display: flex;
    justify-content: center;
    margin-top: 20px;
  }
  
  .tab {
    padding: 10px 20px;
    background-color: #f0f0f0;
    cursor: pointer;
    margin-right: 10px;
  }
  
  .tab.active {
    background-color: #ccc;
  }
  </style>
  