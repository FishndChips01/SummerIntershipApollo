<template>
    <div>
      <ul>
        <li v-for="item in items" :key="item.id">{{ item.name }}</li>
      </ul>
    </div>
  </template>
  
  <script>
import axios from 'axios';

export default {
  data() {
    return {
      tweets: [],
      newTweetContent: ''
    };
  },
  mounted() {
    this.getTweets();
  },
  methods: {
    getTweets() {
      axios.get('http://localhost:3001/comment')
        .then(response => {
          this.tweets = response.data;
        })
        .catch(error => {
          console.error('Error getting tweets:', error.message);
        });
    },
    createTweet() {
      axios.post('http://localhost:3001/comment', { content: this.newTweetContent })
        .then(response => {
          this.getTweets();
          this.newTweetContent = '';
        })
        .catch(error => {
          console.error('Error creating tweets:', error.message);
        });
    }
  }
};
</script>

<style></style>
  