<template>
  <div class="container mx-auto mt-8 px-4">
    <!-- Breadcrumb with enhanced styling -->
    <nav aria-label="breadcrumb" class="mb-6">
      <ol class="flex items-center space-x-2 text-gray-700">
        <li>
          <router-link to="/HomePage" class="text-blue-600 hover:text-blue-800 font-semibold flex items-center">
            <!-- <span class="mr-1">🏠</span>  -->
             Home
          </router-link>
        </li>
        <li><span class="text-gray-400">/</span></li>
        <li>
          <router-link to="/MagazineSubscribers" class="text-blue-600 hover:text-blue-800 font-semibold">
            Subscribers
          </router-link>
        </li>
        <li><span class="text-gray-400">/</span></li>
        <li class="text-gray-500 font-semibold" aria-current="page">{{ subscriber.name }}</li>
      </ol>
    </nav>

    <!-- Enhanced Subscriber Details Card -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
      <!-- Main Info Card -->
      <div class="lg:col-span-2">
        <div class="bg-white rounded-xl shadow-lg p-6">
          <div class="flex items-center justify-between mb-6">
            <h2 class="text-3xl font-bold text-gray-800">{{ subscriber.name }}</h2>
            <span class="px-4 py-2 bg-blue-100 text-blue-800 rounded-full text-sm font-semibold">
              #{{ subscriber.registration_number }}
            </span>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="space-y-4">
              <div class="flex items-center">
                <span class="text-gray-500 w-24">Address:</span>
                <span class="text-gray-800 font-medium">{{ subscriber.address }}</span>
              </div>
              <div class="flex items-center">
                <span class="text-gray-500 w-24">City/Town:</span>
                <span class="text-gray-800 font-medium">{{ subscriber.city_town }}</span>
              </div>
              <div class="flex items-center">
                <span class="text-gray-500 w-24">State:</span>
                <span class="text-gray-800 font-medium">{{ subscriber.state }}</span>
              </div>
              <div class="flex items-center">
                <span class="text-gray-500 w-24">Pincode:</span>
                <span class="text-gray-800 font-medium">{{ subscriber.pincode }}</span>
              </div>
            </div>
            <div class="space-y-4">
              <div class="flex items-center">
                <span class="text-gray-500 w-24">Phone:</span>
                <span class="text-gray-800 font-medium">{{ subscriber.phone }}</span>
              </div>
              <div class="flex items-center">
                <span class="text-gray-500 w-24">Email:</span>
                <span class="text-gray-800 font-medium">{{ subscriber.email }}</span>
              </div>
              <div class="flex items-center">
                <span class="text-gray-500 w-24">Category:</span>
                <span class="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm font-medium">
                  {{ getCategoryName(subscriber.category) }}
                </span>
              </div>
              <div class="flex items-center">
                <span class="text-gray-500 w-24">Type:</span>
                <span class="px-3 py-1 bg-purple-100 text-purple-800 rounded-full text-sm font-medium">
                  {{ getTypeName(subscriber.stype) }}
                </span>
              </div>
            </div>
          </div>
          <div class="mt-6 pt-6 border-t border-gray-200">
            <span class="text-gray-500">Notes:</span>
            <p class="mt-2 text-gray-800">{{ subscriber.notes || 'No notes available' }}</p>
          </div>
        </div>
      </div>

      <!-- Quick Stats Card -->
      <div class="lg:col-span-1">
        <div class="bg-white rounded-xl shadow-lg p-6">
          <h3 class="text-xl font-semibold text-gray-800 mb-4">Subscription Summary</h3>
          <div class="space-y-4">
            <div class="bg-blue-50 rounded-lg p-4">
              <div class="text-sm text-blue-600">Active Subscriptions</div>
              <div class="text-2xl font-bold text-blue-800">{{ activeSubscriptions.length }}</div>
            </div>
            <div class="bg-gray-50 rounded-lg p-4">
              <div class="text-sm text-gray-600">Inactive Subscriptions</div>
              <div class="text-2xl font-bold text-gray-800">{{ inactiveSubscriptions.length }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Add Subscription Button -->
    <button 
      class="bg-gradient-to-r from-blue-600 to-blue-700 text-white px-6 py-3 rounded-lg shadow-lg hover:from-blue-700 hover:to-blue-800 transition duration-200 mb-6 flex items-center"
      @click="openAddSubscriptionModal"
    >
      <span class="mr-2">+</span> Add New Subscription
    </button>

    <!-- Enhanced Tabs -->
    <div class="bg-white rounded-xl shadow-lg mb-8">
      <div class="border-b border-gray-200">
        <ul class="flex -mb-px">
          <li class="mr-2">
            <button 
              class="inline-block py-4 px-6 text-sm font-medium transition duration-200"
              :class="{ 
                'border-b-2 border-blue-600 text-blue-600': activeTab === 'active',
                'text-gray-500 hover:text-blue-600': activeTab !== 'active'
              }"
              @click="activeTab = 'active'"
            >
              Active Subscriptions
            </button>
          </li>
          <li>
            <button 
              class="inline-block py-4 px-6 text-sm font-medium transition duration-200"
              :class="{ 
                'border-b-2 border-blue-600 text-blue-600': activeTab === 'inactive',
                'text-gray-500 hover:text-blue-600': activeTab !== 'inactive'
              }"
              @click="activeTab = 'inactive'"
            >
              Inactive Subscriptions
            </button>
          </li>
        </ul>
      </div>

      <!-- Subscription Tables -->
      <div class="p-6">
        <div v-show="activeTab === 'active'">
          <table class="min-w-full divide-y divide-gray-200">
            <thead>
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Start Date</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">End Date</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Plan</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Payment</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="subscription in activeSubscriptions" :key="subscription._id" class="hover:bg-gray-50">
                <td class="px-6 py-4 text-sm text-gray-900">{{ formatDate(subscription.start_date) }}</td>
                <td class="px-6 py-4 text-sm text-gray-900">{{ formatDate(subscription.end_date) }}</td>
                <td class="px-6 py-4 text-sm text-gray-900">{{ getPlanName(subscription.subscription_plan) }}</td>
                <td class="px-6 py-4 text-sm">
                  <span :class="`px-3 py-1 rounded-full text-xs font-medium ${getStatusColor(subscription.payment_status)}`">
                    {{ subscription.payment_status }}
                  </span>
                </td>
                <td class="px-6 py-4 text-sm text-gray-900">{{ getPaymentModeName(subscription.payment_mode) }}</td>
                <td class="px-6 py-4 text-sm text-gray-900">{{ formatDate(subscription.payment_date) }}</td>
                <td class="px-6 py-4 text-sm">
                  <button 
                    class="bg-gray-100 text-gray-700 px-4 py-2 rounded-md text-xs font-medium hover:bg-gray-200 transition duration-200"
                    @click="openEditSubscriptionModal(subscription)"
                  >
                    Edit
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <div v-show="activeTab === 'inactive'" class="overflow-x-auto">
          <!-- Same table structure as active subscriptions -->
        </div>
      </div>
    </div>

    <!-- Modals and Toast -->
    <add-edit-subscription-modal
      :show="showAddEditSubscriptionModal"
      :subscription="currentSubscription"
      :subscription-plans="subscriptionPlans"
      :payment-modes="paymentModes"
      @close="closeAddEditSubscriptionModal"
      @save="saveSubscription"
    />
    <toast-notification ref="toast" />
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import addEditSubscriptionModal from './AddEditSubscriptionModal.vue';
import magazineSubscriberService from '../services/magazineSubscriberService';
import subscriptionPlanService from '../services/subscriptionPlanService';
import paymentModeService from '../services/paymentModeService';
import subscriptionService from '../services/subscriptionService';
import ToastNotification from './ToastNotification.vue';

export default defineComponent({
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
  // ... rest of the component logic remains the same ...
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
      if (!date) return '';
      const d = new Date(date);
      return `${String(d.getDate()).padStart(2, '0')}/${String(d.getMonth() + 1).padStart(2, '0')}/${d.getFullYear()}`;
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
    },
    getStatusColor(status) {
      const colors = {
        'Paid': 'bg-green-100 text-green-800',
        'Pending': 'bg-yellow-100 text-yellow-800',
        'Overdue': 'bg-red-100 text-red-800',
        'Cancelled': 'bg-gray-100 text-gray-800'
      };
      return colors[status] || 'bg-gray-100 text-gray-800';
    }
  }
});
</script>