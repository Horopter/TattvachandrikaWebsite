<template>
  <div class="container mx-auto mt-8 px-4">
    <!-- Breadcrumb -->
    <nav aria-label="breadcrumb" class="mb-6">
      <ol class="flex space-x-2 text-gray-700">
        <li>
          <router-link to="/HomePage" class="text-blue-600 hover:text-blue-800 font-semibold">Home</router-link>
        </li>
        <li>
          <span>/</span>
        </li>
        <li>
          <router-link to="/MagazineSubscribers" class="text-blue-600 hover:text-blue-800 font-semibold">Subscribers</router-link>
        </li>
        <li>
          <span>/</span>
        </li>
        <li class="text-gray-500 font-semibold" aria-current="page">{{ subscriber.name }}</li>
      </ol>
    </nav>

    <!-- Subscriber Details -->
    <h2 class="text-3xl font-bold text-gray-800 mb-6">{{ subscriber.name }}</h2>
    <div class="bg-white shadow-md rounded-lg p-6 mb-6">
      <div class="space-y-2">
        <p><strong>Registration Number:</strong> <span class="text-gray-600">{{ subscriber.registration_number }}</span></p>
        <p><strong>Address:</strong> <span class="text-gray-600">{{ subscriber.address }}</span></p>
        <p><strong>City/Town:</strong> <span class="text-gray-600">{{ subscriber.city_town }}</span></p>
        <p><strong>State:</strong> <span class="text-gray-600">{{ subscriber.state }}</span></p>
        <p><strong>Pincode:</strong> <span class="text-gray-600">{{ subscriber.pincode }}</span></p>
        <p><strong>Phone:</strong> <span class="text-gray-600">{{ subscriber.phone }}</span></p>
        <p><strong>Email:</strong> <span class="text-gray-600">{{ subscriber.email }}</span></p>
        <p><strong>Category:</strong> <span class="text-gray-600">{{ getCategoryName(subscriber.category) }}</span></p>
        <p><strong>Type:</strong> <span class="text-gray-600">{{ getTypeName(subscriber.stype) }}</span></p>
        <p><strong>Notes:</strong> <span class="text-gray-600">{{ subscriber.notes }}</span></p>
      </div>
    </div>

    <!-- Add Subscription Button -->
    <button class="bg-gradient-to-r from-blue-500 to-blue-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-gradient-to-l transition duration-200 mb-4" @click="openAddSubscriptionModal">Add Subscription</button>

    <!-- Tabs for Active and Inactive Subscriptions -->
    <ul class="flex border-b border-gray-300 mb-4">
      <li class="mr-4">
        <button class="py-2 px-6 font-medium text-gray-600 hover:text-blue-600 transition duration-200" :class="{ 'border-b-2 border-blue-600 text-blue-600': activeTab === 'active' }" @click="activeTab = 'active'">Active Subscriptions</button>
      </li>
      <li>
        <button class="py-2 px-6 font-medium text-gray-600 hover:text-blue-600 transition duration-200" :class="{ 'border-b-2 border-blue-600 text-blue-600': activeTab === 'inactive' }" @click="activeTab = 'inactive'">Inactive Subscriptions</button>
      </li>
    </ul>

    <div class="tab-content">
      <!-- Active Subscriptions Tab -->
      <div v-show="activeTab === 'active'">
        <table class="min-w-full divide-y divide-gray-200 shadow-md">
          <thead class="bg-gray-100">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Start Date</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">End Date</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Subscription Plan</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Payment Status</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Payment Mode</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Payment Date</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="subscription in activeSubscriptions" :key="subscription._id" class="hover:bg-gray-50 transition duration-200">
              <td class="px-6 py-4 text-sm text-gray-900">{{ formatDate(subscription.start_date) }}</td>
              <td class="px-6 py-4 text-sm text-gray-900">{{ formatDate(subscription.end_date) }}</td>
              <td class="px-6 py-4 text-sm text-gray-900">{{ getPlanName(subscription.subscription_plan) }}</td>
              <td class="px-6 py-4 text-sm text-gray-900">{{ subscription.payment_status }}</td>
              <td class="px-6 py-4 text-sm text-gray-900">{{ getPaymentModeName(subscription.payment_mode) }}</td>
              <td class="px-6 py-4 text-sm text-gray-900">{{ formatDate(subscription.payment_date) }}</td>
              <td class="px-6 py-4 text-sm text-gray-900">
                <button class="bg-gray-600 text-white px-4 py-1 rounded-md text-xs shadow-sm hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-500" @click="openEditSubscriptionModal(subscription)">Edit</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Inactive Subscriptions Tab -->
      <div v-show="activeTab === 'inactive'">
        <table class="min-w-full divide-y divide-gray-200 shadow-md">
          <thead class="bg-gray-100">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Start Date</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">End Date</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Subscription Plan</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Payment Status</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Payment Mode</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Payment Date</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="subscription in inactiveSubscriptions" :key="subscription._id" class="hover:bg-gray-50 transition duration-200">
              <td class="px-6 py-4 text-sm text-gray-900">{{ formatDate(subscription.start_date) }}</td>
              <td class="px-6 py-4 text-sm text-gray-900">{{ formatDate(subscription.end_date) }}</td>
              <td class="px-6 py-4 text-sm text-gray-900">{{ getPlanName(subscription.subscription_plan) }}</td>
              <td class="px-6 py-4 text-sm text-gray-900">{{ subscription.payment_status }}</td>
              <td class="px-6 py-4 text-sm text-gray-900">{{ getPaymentModeName(subscription.payment_mode) }}</td>
              <td class="px-6 py-4 text-sm text-gray-900">{{ formatDate(subscription.payment_date) }}</td>
              <td class="px-6 py-4 text-sm text-gray-900">
                <button class="bg-gray-600 text-white px-4 py-1 rounded-md text-xs shadow-sm hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-500" @click="openEditSubscriptionModal(subscription)">Edit</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Add/Edit Subscription Modal -->
    <add-edit-subscription-modal
      :show="showAddEditSubscriptionModal"
      :subscription="currentSubscription"
      :subscription-plans="subscriptionPlans"
      :payment-modes="paymentModes"
      @close="closeAddEditSubscriptionModal"
      @save="saveSubscription"
    />

    <!-- Toast Notification -->
    <toast-notification ref="toast" />
  </div>
</template>

<script>
import addEditSubscriptionModal from './AddEditSubscriptionModal.vue';
import magazineSubscriberService from '../services/magazineSubscriberService';
import subscriptionPlanService from '../services/subscriptionPlanService';
import paymentModeService from '../services/paymentModeService';
import subscriptionService from '../services/subscriptionService';
import ToastNotification from './ToastNotification.vue';

export default {
  components: {
    addEditSubscriptionModal,
    ToastNotification
  },
  data() {
    return {
      subscriber: {},
      activeSubscriptions: [],
      inactiveSubscriptions: [],
      subscriptionPlans: [],
      paymentModes: [],
      categories: [],
      types: [],
      showAddEditSubscriptionModal: false,
      currentSubscription: null,
      activeTab: 'active' // Track the currently active tab
    };
  },
  created() {
    this.loadSubscriber();
    this.loadSubscriptionPlans();
    this.loadPaymentModes();
    this.loadCategories();
    this.loadTypes();
  },
  methods: {
    loadSubscriber() {
      const subscriberId = this.$route.query.id;
      magazineSubscriberService.getMagazineSubscriberById(subscriberId).then(response => {
        this.subscriber = response.data;
        this.loadSubscriptions(subscriberId);
      }).catch(error => {
        this.$refs.toast.showToast('Error retrieving subscribers', 'Error', 'danger');
        console.error("There was an error retrieving the subscriber details!", error);
      });
    },
    loadSubscriptions(subscriberId) {
      subscriptionService.getSubscriptionsBySubscriber(subscriberId).then(response => {
        this.activeSubscriptions = response.data.filter(sub => sub.active);
        this.inactiveSubscriptions = response.data.filter(sub => !sub.active);
      }).catch(error => {
        this.$refs.toast.showToast('Error retrieving subscriptions', 'Error', 'danger');
        console.error("There was an error retrieving the subscriptions!", error);
      });
    },
    loadSubscriptionPlans() {
      subscriptionPlanService.getPlans().then(response => {
        this.subscriptionPlans = response.data;
      }).catch(error => {
        this.$refs.toast.showToast('Error retrieving subscription plans', 'Error', 'danger');
        console.error("There was an error retrieving the subscription plans!", error);
      });
    },
    loadPaymentModes() {
      paymentModeService.getPaymentModes().then(response => {
        this.paymentModes = response.data;
      }).catch(error => {
        this.$refs.toast.showToast('Error retrieving payment modes', 'Error', 'danger');
        console.error("There was an error retrieving the payment modes!", error);
      });
    },
    loadCategories() {
      magazineSubscriberService.getCategories().then(response => {
        this.categories = response.data;
      }).catch(error => {
        this.$refs.toast.showToast('Error retrieving categories', 'Error', 'danger');
        console.error("There was an error retrieving the categories!", error);
      });
    },
    loadTypes() {
      magazineSubscriberService.getTypes().then(response => {
        this.types = response.data;
      }).catch(error => {
        this.$refs.toast.showToast('Error retrieving types', 'Error', 'danger');
        console.error("There was an error retrieving the types!", error);
      });
    },
    openAddSubscriptionModal() {
      this.currentSubscription = {
        subscriber: this.subscriber._id,
        subscription_plan: '',
        payment_status: 'Pending',
        payment_mode: this.paymentModes[0]?.name || '',
        payment_date: ''
      };
      this.showAddEditSubscriptionModal = true;
    },
    openEditSubscriptionModal(subscription) {
      this.currentSubscription = { ...subscription };
      this.showAddEditSubscriptionModal = true;
    },
    closeAddEditSubscriptionModal() {
      this.showAddEditSubscriptionModal = false;
    },
    saveSubscription(subscription) {
      if (subscription._id) {
        subscriptionService.updateSubscription(subscription._id, subscription).then(() => {
          this.loadSubscriptions(this.subscriber._id);
          this.showAddEditSubscriptionModal = false;
        }).catch(error => {
          console.error("There was an error updating the subscription!", error);
        });
      } else {
        subscriptionService.createSubscription(subscription).then(() => {
          this.loadSubscriptions(this.subscriber._id);
          this.showAddEditSubscriptionModal = false;
        }).catch(error => {
          console.error("There was an error creating the subscription!", error);
        });
      }
    },
    formatDate(date) {
      const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
      return new Date(date).toLocaleDateString(undefined, options);
    },
    getPlanName(planId) {
      const plan = this.subscriptionPlans.find(plan => plan._id === planId);
      return plan ? plan.name : '';
    },
    getPaymentModeName(modeId) {
      const mode = this.paymentModes.find(mode => mode._id === modeId);
      return mode ? mode.name : '';
    },
    getCategoryName(categoryId) {
      const category = this.categories.find(cat => cat._id === categoryId);
      return category ? category.name : '';
    },
    getTypeName(typeId) {
      const type = this.types.find(type => type._id === typeId);
      return type ? type.name : '';
    }
  }
};
</script>

<style scoped>
/* No additional styles needed for Tailwind CSS */
</style>
