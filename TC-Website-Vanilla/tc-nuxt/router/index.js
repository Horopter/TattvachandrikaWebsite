import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/views/HomePage.vue';
import SubscriptionModes from '@/views/SubscriptionModes.vue';
import SubscriptionLanguages from '@/views/SubscriptionLanguages.vue';
import SubscriberCategories from '@/views/SubscriberCategories.vue';
import SubscriberTypes from '@/views/SubscriberTypes.vue';
import SubscriptionPlans from '@/views/SubscriptionPlans.vue';
import MagazineSubscribers from '@/views/MagazineSubscribers.vue';
import SubscriberDetails from '@/views/MagazineSubscriberDetails.vue';
import PaymentModes from '@/views/PaymentModes.vue';
import Index from '@/views/index.vue';

const routes = [
  {
    path: '/home',
    name: 'IndexPage',
    component: Index
  },
  {
    path: '/details',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/subscription-modes',
    name: 'SubscriptionModes',
    component: SubscriptionModes
  },
  {
    path: '/subscription-languages',
    name: 'SubscriptionLanguages',
    component: SubscriptionLanguages
  },
  {
    path: '/subscriber-categories',
    name: 'SubscriberCategories',
    component: SubscriberCategories
  },
  {
    path: '/subscriber-types',
    name: 'SubscriberTypes',
    component: SubscriberTypes
  },
  {
    path: '/subscription-plans',
    name: 'SubscriptionPlans',
    component: SubscriptionPlans
  },
  {
    path: '/subscribers',
    name: 'MagazineSubscribers',
    component: MagazineSubscribers
  },
  {
    path: '/subscribers/:id',
    name: 'SubscriberDetails',
    component: SubscriberDetails,
    props: true,
  },
  {
    path: '/payment-modes',
    name: 'PaymentModes',
    component: PaymentModes
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
