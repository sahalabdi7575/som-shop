# Database Setup Instructions

## Overview

This e-commerce application uses Supabase as the backend database. The database schema includes tables for users, products, orders, and order items with proper relationships and security policies.

## Setup Steps

### 1. Create Supabase Project

1. Go to [Supabase](https://supabase.com) and create an account
2. Create a new project
3. Note your project URL and API keys from Settings > API

### 2. Run Migrations

#### Option A: Using Supabase Dashboard (Recommended)

1. Go to your Supabase project dashboard
2. Navigate to the SQL Editor
3. Copy and paste the contents of `001_initial_schema.sql` and execute
4. Repeat for `002_performance_optimizations.sql`

#### Option B: Using Supabase CLI

1. Install Supabase CLI
2. Run: `supabase db push`

### 3. Configure Environment Variables

Create a `.env` file in your project root:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
FLASK_SECRET_KEY=your_flask_secret_key
ADMIN_EMAIL=daymaro94@gmail.com