import { createRouter, createWebHistory } from 'vue-router';
import Comment from '../views/Comment.vue';
import Score from '../views/Score.vue';

const routes = [
  {
    path: '/comment',
    name: 'Comment',
    component: Comment
  },
  {
    path: '/score',
    name: 'Score',
    component: Score
  },
  {
    path: '/',
    redirect: '/comment'
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
