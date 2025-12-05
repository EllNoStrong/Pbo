from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomerRegisterForm, DriverRegisterForm, RestaurantRegisterForm
from .models import User


# =============================
# CUSTOM LOGIN VIEW
# =============================
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        user = form.get_user()
        # jika role driver/resto harus approved
        if hasattr(user, 'role'):
            if user.role in ['driver', 'restaurant'] and not user.is_approved:
                messages.error(self.request, "Akun Anda belum disetujui admin.")
                return redirect('accounts:login')
        return super().form_valid(form)


# =============================
# REGISTRASI
# =============================
def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrasi sukses. Selamat datang!")
            return redirect('home')
    else:
        form = CustomerRegisterForm()
    return render(request, 'accounts/register_customer.html', {'form': form})


def register_driver(request):
    if request.method == 'POST':
        form = DriverRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registrasi driver berhasil. Menunggu persetujuan admin.")
            return redirect('accounts:login')
    else:
        form = DriverRegisterForm()
    return render(request, 'accounts/register_driver.html', {'form': form})


def register_restaurant(request):
    if request.method == 'POST':
        form = RestaurantRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registrasi restoran berhasil. Menunggu persetujuan admin.")
            return redirect('accounts:login')
    else:
        form = RestaurantRegisterForm()
    return render(request, 'accounts/register_restaurant.html', {'form': form})


# =============================
# LOGIN / LOGOUT
# =============================
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Admin masuk ke admin panel
            if user.role == "admin":
                return redirect("accounts:admin_dashboard")

            # Driver
            if user.role == "driver":
                return redirect("drivers:dashboard")

            # Restaurant
            if user.role == "restaurant":
                return redirect("restaurants:dashboard")

            # Customer
            return redirect("home")

        return render(request, "accounts/login.html", {
            "error": "Username atau password salah"
        })

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("accounts:login")


# =============================
# DECORATOR ADMIN
# =============================
def admin_required(view_func):
    return user_passes_test(lambda u: u.is_authenticated and u.role == "admin")(view_func)


# =============================
# DASHBOARD ADMIN
# =============================
@admin_required
def admin_dashboard(request):
    return render(request, "adminpanel/dashboard.html")


# =============================
# APPROVAL AKUN
# =============================
@admin_required
def account_approvals(request):
    pending = User.objects.filter(is_approved=False, role__in=["driver", "restaurant"])
    return render(request, "adminpanel/approvals.html", {"pending": pending})


@admin_required
def approve_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_approved = True
    user.save()
    return redirect("accounts:approvals")


# =============================
# MANAGE DRIVERS
# =============================
@admin_required
def manage_drivers(request):
    drivers = User.objects.filter(role="driver")
    return render(request, "adminpanel/drivers.html", {"drivers": drivers})


# =============================
# MANAGE RESTAURANTS
# =============================
@admin_required
def manage_restaurants(request):
    restos = User.objects.filter(role="restaurant")
    return render(request, "adminpanel/restaurants.html", {"restaurants": restos})


# =============================
# MANAGE ORDERS
# =============================
@admin_required
def manage_orders(request):
    return render(request, "adminpanel/orders.html")


# =============================
# ADMIN CHAT
# =============================
@admin_required
def admin_chat(request):
    return render(request, "adminpanel/chat.html")
